import discord
from discord.ext import commands

import re

class Repeat(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Repeat Online")

  @commands.Cog.listener("on_message")
  async def perroquet(self, message):
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



def setup(client):
  client.add_cog(Repeat(client))