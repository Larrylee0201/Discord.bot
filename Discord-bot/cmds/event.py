from core.classes import Cog_Extension
import discord
from discord import file
from discord.ext import commands
import json
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import command


with open("setting.json","r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["join"]))
        await channel.send(f"{member} 直接閃現進來啦!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["leave"]))
        await channel.send(f"{member} 給我傳送走了欸!")
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = ['show me what u got']
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("I got black I got white, what u want")



def setup(bot):
    bot.add_cog(Event(bot))