import discord
from discord.ext import commands
from core.classes import Cog_Extension


class User_info(Cog_Extension):
    
  @commands.command()
  async def showuser(self,ctx):
    for member in(ctx.channel.members):    
      await ctx.send(member)


  @commands.command()
  async def member_info(self,ctx):
    for member in(ctx.channel.members):
      await ctx.send({member})



 
def setup(bot):
    bot.add_cog(User_info(bot))