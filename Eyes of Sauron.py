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

@app_commands.command(name="list", description="A list of individuals that has been registered in the database")
@app_commands.describe(list="Wanna know who's the real G?")
@app_commands.choices(list=[
    app_commands.Choice(name="Cruncher", value="1"),
    app_commands.Choice(name="Dignity", value="2")
])
async def list_command(interaction: discord.Interaction, list: app_commands.Choice[int]):
    await interaction.response.send_message(f"List selected: {list}")


@bot.tree.command(name="watchlist", description="The Sauron has its eyes on these indiviaduals who has fallen prey.")
async def watchlist(interaction: Interaction):
    view = Menu()
    view.add_item(discord.ui.Button(
        label="Invite Link",
        style=discord.ButtonStyle.link,
        url="https://discord.com/invite/edot",
        emoji="<X_illyria:1018658471236861952>"))
    await interaction.response.send_message("The Watchful Eyes", view=view)
 
@bot.tree.command(name="cruncher", description="Details of Wojiao Cork")
async def cruncher(interaction: Interaction):
    embed = discord.Embed(
        title="Crunchy Cork's Details",
        description="Here are the details of Crunchy Cork:",
        color=discord.Color.blurple()
    )
    embed.set_thumbnail(url="https://tr.rbxcdn.com/30DAY-AvatarHeadshot-D6A22B4D634F4B10E2939FF53CB2927A-Png/150/150/AvatarHeadshot/Png/noFilter")

    embed.add_field(name="Username", value="[Crunchy_Cork](https://www.roblox.com/users/2313514417/profile)", inline=True)
    embed.add_field(name="KPH", value="87.52", inline=True)
    embed.add_field(name="Notes", value="This guy is so hawt, I am drooling looking at his handsome face.", inline=False)
    embed.add_field(name="Affiliation", value="Eagles of Illyria", inline=True)
    embed.add_field(name="Rank", value="155", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Kills", value="84,458", inline=True)
    embed.add_field(name="Hours", value="941", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Normalised Stats", value="", inline=False)
    embed.add_field(name="KPH", value="5.5", inline=True)
    embed.add_field(name="Hours",value="7.85", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Levels",value="8.05", inline=True)
    embed.add_field(name="Kills",value="7.9", inline=True)
    embed.add_field(name="\u200b", value="\u200b", inline=True)
    embed.add_field(name="Data Acquired", value="11th September 2023", inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/1216630854957404203/1222804174564233256/image.png?ex=66178c21&is=66051721&hm=9583937218b7018ae3de6cc81871640a3d1d194d67301058084fe75c25b5f5fe&")
    embed.set_footer(text="Powered by the all powerful Eyes of Sauron")
    
    await interaction.response.send_message(embed=embed)

bot.run(BOT_TOKEN)
