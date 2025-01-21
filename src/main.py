import discord
from discord.ext import commands

import requests
import bot_secrets

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="/", intents=intents)

bot.commands.add("hola")

@bot.command()
async def hola(ctx, *args):
    await ctx.send(f"hola {args}")

@bot.event
async def on_ready():
    print(f"{bot.user} RDY")

bot.run(bot_secrets.API_TOKEN)