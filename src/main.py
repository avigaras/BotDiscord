import discord
from discord.ext import commands

import requests
import os

import webserver


API_TOKEN = os.getenv("API_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="/", intents=intents)

bot.commands.add("hola")

@bot.command()
async def hola(ctx, *args):
    await ctx.send(f"hola {args}")

@bot.event
async def on_ready():
    print(f"{bot.user} RDY")

webserver.keep_alive()
bot.run(API_TOKEN)