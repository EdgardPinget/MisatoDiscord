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
    await l33t(message)

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

# Mettre les dictionnaires dans un fichier annexe, et permettre la gestion de plusieurs commandes de l33t
async def l33t(message):

    basic_leet = {
      ord("a"): "4",
      ord("A"): "4",
      ord("e"): "3",
      ord("E"): "3",
      ord("i"): "1",
      ord("I"): "1",
      ord("o"): "0",
      ord("O"): "0",
      ord("s"): "5",
      ord("S"): "5",
      ord("g"): "6",
      ord("G"): "6",
      ord("t"): "7",
      ord("T"): "7",
      ord("v"): "\\\/",
      ord("V"): "\\\/",
      }
    if message.content.startswith("!l33t"):
      message_cut = message.content[5:]
      message_final = message_cut.translate(basic_leet)
      await message.channel.send(message_final)


client.run(os.getenv('TOKEN'))
