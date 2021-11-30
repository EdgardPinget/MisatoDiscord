import discord
from discord.ext import commands

class Encode(commands.Cog):

  def __init__(self, client):
    self.client = client

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot Online")
    
  #Commands
  @commands.command(name="l33t")
  async def l33t(self, ctx, *, arg):
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
      ord("V"): "\\\/"
      }
    print("passé")
    message_cut = arg
    message_final = message_cut.translate(basic_leet)
    
    await ctx.send(message_final)


def setup(client):
  client.add_cog(Encode(client))