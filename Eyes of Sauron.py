from discord.ext import commands
from discord import app_commands
import discord
from discord.ui import Select, View
import config
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_option
from discord_slash.model import SlashCommandOptionType

BOT_TOKEN = config.TOKEN
CHANNEL_ID = 1216630854957404203

bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())

class DataView(View):
    def __init__(self, options):
        super().__init__()
        self.add_item(Select(placeholder="Choose your peeps.", options=options))

@bot.event
async def on_ready():
    print("Wojiao Cork...")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Wojiao Cork....")

@bot.tree.command(name="help")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This bot is created by the Ministry of Numbers with the purpose of having each database for users that has submitted their data to us for further studies. So far, about 100+ individuals have their data recorded and saved inside the database, The Eyes of Sauron.", ephemeral=True)

@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")

@bot.tree.command(name="data")
async def data(interaction: discord.Interaction):
    data = ["item1", "item2", "item3", "item4"]
    formatted_data = "\n".join(data)
    await interaction.response.send_message(f"Here is the data: \n ```{formatted_data}```")

@bot.command()
async def hello(ctx):
    await ctx.send("Database for Entrenched, Rojtar eyes only...")

@bot.command(name="chosen")
async def chosen(ctx):
        options=[
            discord.SelectOption(
                label="Crunchy", 
                emoji=":cloudy:", 
                description="Handsome man"),
            discord.SelectOption(
                label="Diggitty",
                emoji=":target:", 
                description="Recon Nation")
        ]
        view = DataView(options)
        await ctx.send(f"Congratulations {ctx.author.name}. The one you've chosen are...", view=view)

bot.run(BOT_TOKEN)
