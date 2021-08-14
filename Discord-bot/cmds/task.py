from core.classes import Cog_Extension
import discord
from discord.ext import commands
import json,asyncio,datetime


class Task(Cog_Extension):
  def __init__(self,*args,**krawgs):
    super().__init__(*args,**krawgs)

    async def interval():
      await self.bot.wait_unil_ready()
      self.channel = self.bot.get_channel(858743639269441536)
      while not self.bot.is_closed():
        await self.channel.send("Hi I'm Bot")
        await asyncio.sleep(5)
    self.bg_task = self.bot.loop.create_task(interval())


  @commands.command()
  async def set_channel(self,ctx,ch:int):
      self.channel = self.bot.get_channel(ch)
      await ctx.send(f"Set_Channel:{self.channel.mention}")

                


def setup(bot):
    bot.add_cog(Task(bot))