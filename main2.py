import discord
#imports
r=0
import os
import time
from datetime import datetime
import asyncio
import datetime as dt
from discord.ext import commands, tasks
intents = discord.Intents(members =True,messages=True, guilds=True)
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DTOKEN')
GUILD = os.getenv('GTOKEN')
client = discord.Client()
bot = commands.Bot(command_prefix='$')#Sets prefix for commands(!Command)
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
#Await word then delete said word leaving the remainder fo the message
image_types = ["png", "jpeg", "gif", "jpg"]