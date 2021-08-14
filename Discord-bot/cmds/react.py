import discord
from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    
    @commands.command()
    async def get(self,ctx):
        await ctx.send("I got black I got white, what u want")

    @commands.command()
    async def picture(self,ctx):
        pic = discord.File("https://i.ytimg.com/vi/5qap5aO4i9A/maxresdefault.jpg")
        await ctx.send(file = pic)

 
def setup(bot):
    bot.add_cog(React(bot))