# External Libraries
from discord import Embed
from discord.ext import commands

# Globals and Internal Files
from nominee_selector import NomineeSelector


class NominateCog(commands.Cog, name="Nominate"):

  def __init__(self, bot):
    self.bot = bot

  # Check if the user is allowed to use an admin-only slash command
  def is_admin(ctx):
    if "exec" in [role.name for role in ctx.user.roles]:
      return True
    return False

  ########## ADMIN ONLY COMMANDS ##########

  # MOVIE NOMINATION
  @commands.hybrid_command(
    name="nominate_film",
    description="Nominate for Movie of the Month (ADMIN ONLY)")
  @commands.check(is_admin)
  async def nominate_film(self, ctx):
    # Get nominees
    nominees = NomineeSelector.nominate(True)

    # Send to embed
    await self.UFS_cmd_nominate(ctx, nominees, True)

  # MUSIC NOMINATION
  @commands.hybrid_command(
    name="nominate_music",
    description="Nominate for Music of the Week (ADMIN ONLY)")
  @commands.check(is_admin)
  async def nominate_music(self, ctx):
    nominees = NomineeSelector.nominate(False)
    await self.UFS_cmd_nominate(ctx, nominees, False)

  # Error if not admin
  @nominate_film.error
  @nominate_music.error
  async def say_error(ctx, error):
    await ctx.send(
      "You must be an admin to use this command", ephemeral=True)

  # Embed Selected MotW/AotW Nominees and Send to Channel
  async def UFS_cmd_nominate(ctx, nominees, nominee_type):
    # Initialize empty pings and embed object
    ping_users = ""
    embed = Embed()

    # Determine author from nomine type
    if nominee_type:
      embed.set_author(name="Movie Nominees")
    else:
      embed.set_author("Music Winner")

    # Embed to Message and Ping
    for i, nominee in enumerate(nominees, 1):
      embed.add_field(name="Nominee #{}".format(i), value=nominee.name(), inline=False) # Add member
      ping_users += "<@" + nominee.discord_ID() + ">" + " " # Add to ping

    # Send Winners
    await ctx.send(embed=embed, content=ping_users)