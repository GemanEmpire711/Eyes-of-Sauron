from discord.ext import commands
import discord

BOT_TOKEN = "MTIxNjYyNjU3OTIxMjQ3MjM4MA.G81oUg.tYrk-KpOoxeOKCvzzHT4JjFW43v_KwUBcxoziI"
CHANNEL_ID = 1216630854957404203

bot = commands.Bot(command_prefix="@", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Wojiao Cork...")

bot.run(BOT_TOKEN)