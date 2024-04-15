# main.py

import os
import csv
import io

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1na55MFMJhx13D5zozeea0px1XrMc4UPVsMYSEpY3jgU"

def organize_csv_data():
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(credentials.to_json())

    try:
        service = build("sheets", "v4", credentials=credentials)
        sheets = service.spreadsheets()

        result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range="Databass!A1:K170").execute()
        values = result.get("values", [])

        csv_data = {}
        for i, row in enumerate(values, start=1):
            csv_data[i] = row

        return csv_data

    except HttpError as error:
        print(error)

if __name__ == "__main__":
    organize_csv_data()
