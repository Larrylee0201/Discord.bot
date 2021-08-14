import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension

class Channel(Cog_Extension):

 @commands.command() 
 async def textchannel(self,ctx):
   for textchannel in(ctx.guild.text_channels):
      await ctx.send(textchannel)

 @commands.command() 
 async def textchannel_info(self,ctx):
   for textchannel_info in(ctx.guild.text_channels):
      await ctx.send({textchannel_info})


 @commands.command() 
 async def voicechannel(self,ctx):
   for voicechannel in(ctx.guild.voice_channels):
      await ctx.send(voicechannel)

 @commands.command() 
 async def voicechannel_info(self,ctx):
   for voicechannel_info in(ctx.guild.voice_channels):
      await ctx.send({voicechannel_info})


def setup(bot):
    bot.add_cog(Channel(bot))