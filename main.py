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

async def perroquet(message):
    regex_di_start = "[dD]i[ts]?"
    regex_di_end = "[,;.?!]"

    #On cherche un "di" dans le message
    match_start = re.search(regex_di_start, message.content)
    if match_start and ("http" not in message.content):
        # On va essayer de couper le message à la prochaine ponctuation.
        reply_start = message.content[match_start.end():]

        reply_limit = re.search(regex_di_end, reply_start)
        if reply_limit:
            message_final = reply_start[:reply_limit.end()]          
        else:
            message_final = reply_start

        await message.channel.send(message_final)

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))
