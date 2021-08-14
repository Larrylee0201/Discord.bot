import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension
import datetime

class Help(Cog_Extension):


 @commands.command()
 async def help(self,ctx):
     embed=discord.Embed(title="Commands Description",description="prefix is '~'\nofa=only for administrator",color=0xa65430, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/M3ViMwT.jpg")
     embed.add_field(name="`bd`", value="Link of BetterDiscord", inline=True)
     embed.add_field(name="`opgg`", value="Link of OP.GG", inline=True)
     embed.add_field(name="`github`", value="Link of GitHub", inline=True)
     embed.add_field(name="`yt`", value="Link of Youtube", inline=True)
     embed.add_field(name="`lols11`", value="LOL S11 information", inline=True)
     embed.add_field(name="`ping`", value="Show ping", inline=True)
     embed.add_field(name="`say`", value="Type what you want to say and let bot do it", inline=True)
     embed.add_field(name="`clean`(ofa)", value="Type the number of messages to be cleaned up after this command",inline=True)
     embed.add_field(name="`purge`(ofa)", value="Clean up all messages", inline=True)
     embed.add_field(name="`member_info`", value="Show all information of this channel", inline=True)
     embed.add_field(name="`showuser`", value="Show user's name and discriminator who is in this channel(text)", inline=True)
     embed.add_field(name="`textchanneel`", value="Show all textchannel", inline=True)
     embed.add_field(name="`textchanneel_info`", value="Show all textchannel's information", inline=True)
     embed.add_field(name="`voicechanneel`", value="Show all voicechannel", inline=True)
     embed.add_field(name="`voicechanneel_info`", value="Show all voicechannel's information", inline=True)
     embed.add_field(name="`mute`(ofa)", value="mute someone you choose", inline=True)
     embed.add_field(name="`unmute`(ofa)", value="mute someone you choose", inline=True)
     embed.add_field(name="`load`(ofa)", value="load extention", inline=True)
     embed.add_field(name="`unload`(ofa)", value="unload extention", inline=True)
     embed.add_field(name="`reload`(ofa)", value="reload extention", inline=True)
     await ctx.send(embed=embed)
     


 


def setup(bot):
    bot.add_cog(Help(bot))