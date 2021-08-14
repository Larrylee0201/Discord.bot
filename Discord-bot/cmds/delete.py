import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension
from discord import User

class Delete(Cog_Extension):
 @commands.command()
 async def say(self,ctx,*,msg):
     await ctx.message.delete()
     await ctx.send(msg)

 @commands.command()
 @commands.has_permissions(administrator=True)
 async def clean(self,ctx,num:int):
     await ctx.channel.purge(limit=num+1)
     await ctx.send(f"`Cleaned {num} messages.`")

 @commands.command()
 @commands.has_permissions(administrator=True)
 async def purge(self,ctx):
     await ctx.channel.purge(limit=None)
     await ctx.send("`Messege cleaned.`")

  




def setup(bot):
    bot.add_cog(Delete(bot))