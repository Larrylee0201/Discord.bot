import discord
from discord import file
from discord.ext import commands
import json
import os
import keep_alive

client = discord.Client()

intents = discord.Intents.default()
intents.members = True

with open("setting.json","r",encoding="utf8") as jfile:
    jdata = json.load(jfile)

bot =  commands.Bot(command_prefix='~',intents = intents,help_command=None)

@bot.event
async def on_ready():
    print("<< Bot is online >>",)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="~purge"))


@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unloaded {extension} done.")

@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reloaded {extension} done.")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")




if __name__ == "__main__":
    keep_alive.keep_alive()
    bot.run(jdata["BOT SECRET"])
