from discord.ext import commands
from discord import app_commands
from discord import Interaction
import discord
from discord.ui import Select, View
import config

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

class DataView(View):
    def __init__(self, options):
        super().__init__()
        self.add_item(Select(placeholder="Choose your peeps.", options=options))

@bot.event
async def on_ready():
    await bot.tree.sync()
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

@bot.tree.command(name="ping", description="It wukk show the ping")
async def ping(interaction : Interaction):
    bot_latency = round(bot.latency*1000)
    await interaction.response.send_message(f"Pong... {bot_latency}ms")

@bot.command()
async def hello(ctx):
    await ctx.send("Database for Entrenched, Rojtar eyes only...")

@bot.command()
async def menu(ctx):
     view = Menu()
     view.add_item(discord.ui.Button(
         label="discord invite link", 
         style=discord.ButtonStyle.link, 
         url="https://discord.com/invite/edot", 
         emoji="<X_illyria:1018658471236861952>"))
     await ctx.reply("The watchful eyes", view=view)
 
@bot.tree.command(name="chosen", description="The best one")
async def chosen(interaction : Interaction):
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
        await interaction.response.send_message(f"Congratulations {interaction.user.mention}. The one you've chosen are...", view=view)
        # I give up

bot.run(BOT_TOKEN)
