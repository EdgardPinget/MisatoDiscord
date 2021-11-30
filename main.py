import discord
import os
from discord.ext import commands

import re

#Keep bot online with continuous ping
from tools import keep_alive as ka

ka.keep_alive()

client = commands.Bot(command_prefix = '!')

@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
