import discord
import os

import re

#Keep bot online with continuous ping
from tools import keep_alive as ka

ka.keep_alive()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await perroquet(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


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


client.run(os.getenv('TOKEN'))
