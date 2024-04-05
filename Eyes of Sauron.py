import discord
from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord.ui import Select, View
import config
import database as d

BOT_TOKEN = config.TOKEN
CHANNEL_ID = 1216630854957404203

bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())

class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Misc", style=discord.ButtonStyle.grey)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Hello, this is a Misc.")

    @discord.ui.button(label="Context", style=discord.ButtonStyle.green)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="I wanna end it all")
    
    @discord.ui.button(label="Eyes of Sauron", style=discord.ButtonStyle.blurple)
    async def menu3(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.embeds(color=discord.Color.random())
        embed.set_author(name=f"Gandalf")
        embed.add_field(name="COK", value="Cock")
        await interaction.response.edit_message(embed=embed)

    @discord.ui.button(label="I give up", style=discord.ButtonStyle.red)
    async def menu4(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.embeds(color=discord.Color.random())
        embed.set_author(name=f"Gock")
        embed.add_field(name="Cruncher", value="Cock")
        await interaction.response.edit_message(embed=embed)
        self.value
        self.stop

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Wojiao Cork...")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Wojiao Cork....")

@bot.command()
async def menu(ctx):
     view = Menu()
     view.add_item(discord.ui.Button(
         label="discord invite link", 
         style=discord.ButtonStyle.link, 
         url="https://discord.com/invite/edot", 
         emoji="<X_illyria:1018658471236861952>"))
     await ctx.reply("The watchful eyes", view=view)

@bot.command()
async def hello(ctx):
    await ctx.send("Database for Entrenched, Rojtar eyes only...")

@bot.tree.command(name="help")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hey {interaction.user.mention}! This bot is created by the Ministry of Numbers with the purpose of having each database for users that has submitted their data to us for further studies. So far, about 100+ individuals have their data recorded and saved inside the database, The Eyes of Sauron.", ephemeral=True)

@bot.tree.command(name="list", description="Database for several individuals in Entrenched.")
@app_commands.choices(list=[
    discord.app_commands.Choice(name="Cruncher", value=1),
    discord.app_commands.Choice(name="Dignity", value=2)
])
async def list(interaction: discord.Interaction, list: int):
    if list == 1:
        await d.cruncher(interaction.response)
    elif list == 2:
        await d.dignity(interaction.response)


@bot.tree.command(name="watchlist", description="The Sauron has its eyes on these indiviaduals who has fallen prey.")
async def watchlist(interaction: Interaction):
    view = Menu()
    view.add_item(discord.ui.Button(
        label="Invite Link",
        style=discord.ButtonStyle.link,
        url="https://discord.com/invite/edot",
        emoji="<X_illyria:1018658471236861952>"))
    await interaction.response.send_message("The Watchful Eyes", view=view)

bot.run(BOT_TOKEN)
