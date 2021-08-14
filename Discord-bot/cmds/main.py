#Embed
import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension
import datetime

class Main(Cog_Extension):

 @commands.command()
 async def ping(self,ctx):
    await ctx.send(f"{round(self.bot.latency*1000)}(ms)")

 @commands.command()
 async def lols11(self,ctx):
     embed=discord.Embed(title="S11 League of Legends", url="https://www.youtube.com/watch?v=e4ExWS6OQ_A", description="League of Legends every season update info-video", color=0x4055a0, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/LXmMT8i.png")
     embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/LoL_icon.svg/1200px-LoL_icon.svg.png")
     embed.add_field(name="date ", value="create time:2021/7/1", inline=True)
     embed.set_footer(text="Have a good rank")
     await ctx.send(embed=embed)

 @commands.command()
 async def opgg(self,ctx):
     embed=discord.Embed(title="OP.GG", url="https://tw.op.gg/", description="check info on op.gg", color=0x4055a0, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/LXmMT8i.png")
     embed.set_thumbnail(url="https://opgg-static.akamaized.net/icon/reverse.rectangle.png")
     embed.add_field(name="date ", value="create time:2021/7/7", inline=True)
     embed.set_footer(text="Have a good rank")
     await ctx.send(embed=embed)

 @commands.command()
 async def yt(self,ctx):
     embed=discord.Embed(title="Youtube", url="https://www.youtube.com/", description="Nothing here", color=0xca1c1c, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/LXmMT8i.png")
     embed.set_thumbnail(url="https://frankchiu.io/wp-content/uploads/2020/01/youtube_logo_dark.jpg")
     embed.add_field(name="date ", value="create time:2021/7/7", inline=True)
     embed.set_footer(text="Have a good day")
     await ctx.send(embed=embed)
 @commands.command()
 async def bd(self,ctx):
     embed=discord.Embed(title="better discord", url="https://betterdiscord.app/", description="Nothing here", color=0x4055a0, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/LXmMT8i.png")
     embed.set_thumbnail(url="https://betterdiscord.app/resources/branding/logo_solid.png")
     embed.add_field(name="date ", value="create time:2021/7/14", inline=True)
     embed.set_footer(text="Have a good day")
     await ctx.send(embed=embed)

 @commands.command()
 async def github(self,ctx):
     embed=discord.Embed(title="Github", url="https://github.com/Larrylee0201/Discord.bot", description="Nothing here", color=0xffffff, timestamp= datetime.datetime.utcnow())
     embed.set_author(name="Larry", icon_url="https://i.imgur.com/LXmMT8i.png")
     embed.set_thumbnail(url="https://www.influxdata.com/wp-content/uploads/GitHub-logo.jpg")
     embed.add_field(name="date ", value="create time:2021/7/15", inline=True)
     embed.set_footer(text="Hope it will give u guys some advise")
     await ctx.send(embed=embed)

 



def setup(bot):
    bot.add_cog(Main(bot))  
