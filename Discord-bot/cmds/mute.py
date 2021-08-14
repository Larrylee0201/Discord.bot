import discord
from discord.ext import commands
from discord.ext.commands.cog import Cog
from core.classes import Cog_Extension


class Mute(Cog_Extension):
  #mute  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def mute(self,ctx,member: discord.Member,*,reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles,name="Muted")

    if not mutedRole:
      mutedRole = await guild.create_role(name="Muted")

      for channel in guild.channels:
        await channel.set_premission(mutedRole, speak=False, send_messege=False, read_messege_history=True, read_messeges=False)

    await member.add_roles(mutedRole,reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")




  @commands.command()
  @commands.has_permissions(administrator=True)
  async def unmute(self,ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles,name="Muted")
    
    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmute {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")



  #kick
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def kick(self,ctx,member: discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"Kicked {member.mention} for reason {reason}")
    await member.send(f"You were kick for {reason}")


  #ban
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ban(self,ctx,member: discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"Baned {member.mention} for reason {reason}")
    await member.send(f"You were ban for {reason}")
   


def setup(bot):
    bot.add_cog(Mute(bot))