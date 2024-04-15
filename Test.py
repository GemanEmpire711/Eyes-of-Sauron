import discord
import main

async def process_data(csv_data, position, interaction: discord.Interaction):
    if position in csv_data:
        row_data = csv_data[position]
        # Extract data from the row
        username = row_data[0]
        KPH = row_data[1]
        Notes = row_data[2]
        faction = row_data[3]
        Rank = row_data[4]
        Kills = row_data[5]
        Hours = row_data[6]
        Norm_KPH = row_data[7]
        Norm_Hours = row_data[8]
        Norm_Levels = row_data[9]
        Norm_Kills = row_data[10]
        Dates = row_data[11]
        Graph = row_data[12]

        embed = discord.Embed(
            title=f"{username}",
            description="The Details:",
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=" ")

        embed.add_field(name="Username", value=username, inline=True)
        embed.add_field(name="KPH", value=KPH, inline=True)
        embed.add_field(name="Notes", value=Notes, inline=False)
        embed.add_field(name="Affiliation", value=faction, inline=True)
        embed.add_field(name="Rank", value=Rank, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="Kills", value=Kills, inline=True)
        embed.add_field(name="Hours", value=Hours, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="Normalized Stats", value="", inline=False)
        embed.add_field(name="KPH", value=Norm_KPH, inline=True)
        embed.add_field(name="Hours", value=Norm_Hours, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="Levels", value=Norm_Levels, inline=True)
        embed.add_field(name="Kills", value=Norm_Kills, inline=True)
        embed.add_field(name="\u200b", value="\u200b", inline=True)
        embed.add_field(name="Data Acquired", value=Dates, inline=False)
        embed.set_image(url=Graph)
        embed.set_footer(text="Powered by the all-powerful Eyes of Sauron")
        
        await interaction.response.send_message(embed=embed)
        return embed
    else:
        print("Position {} is not available in the CSV data.".format(position))
        return None

csv_data = main.organize_csv_data()
for position in range(2, 17):
    embed = await process_data(csv_data, position)
