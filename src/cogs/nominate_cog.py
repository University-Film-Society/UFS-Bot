# External Libraries
from discord import Embed
from discord.ext import commands
import numpy

# Internal Files
import parsing_modules.download as Download


class NominateCog(commands.Cog, name="Nominate"):
  """
  Summary
  ----------
  - Cog that contains nomination-related commands.

  ...

  Attributes
  ----------
  - movie_nominee_file (str): filepath to the movie .csv
  - music_nominee_file (str): filepath to the music .csv
  - bot (Bot): discord bot the cog is attached to
  """

  def __init__(self, bot):
    """
    Constructs all the necessary attributes for the nominate cog object
    
    ...

    Args:
    - movie_nominee_file (str): filepath to the movie .csv
    - music_nominee_file (str): filepath to the music .csv
    - bot (Bot): discord bot the cog is attached to
    """
    self.movie_nominee_file = "data/nominees/Movie of the Month.csv"
    self.music_nominee_file = "data/nominees/Music of the Week.csv"
    
    self.bot = bot

  def is_admin(ctx):
    """Check if the user is allowed to use an admin-only slash command

    ...

    Returns:
    - bool: true if the user has an exec role, false otherwise
    
    """
    return True if "exec" in [role.name for role in ctx.user.roles] else False

  def get_probabilities(self, nominees, total):
    """Set the probabilities of being nominated for each user depending on their check

    ...

    Args:
    - nominees (list[Nominee]): list of nominees
    - total (int): number of nominees

    Returns:
    - list: weights related to the nominees
    """

    weights = []
    for nominee in nominees:
      if nominee.check() == 'A':
        # Not previously selected prioritized
        weights.append(50)
        # Previously selected
      if nominee.check() == 'B' or nominee.check() == 'C':
        weights.append(10)

    probabilities = []
    total = sum(weights)
    for weight in weights:
      probabilities.append(weight / total)

    return probabilities

  def nominate(self, nominee_type):
    """Nominates members from the nomination.csv files

    ...

    Args:
    - nominee_type (bool): The type of nomination, True is movie and False is music

    Returns:
    - single item or ndarray : The generated random samples
    """
    week_type = self.movie_nominee_file if nominee_type == True else self.music_nominee_file

    nominees = Download.get_nominees(week_type)
    probabilities = self.get_probabilities(nominees, len(nominees))

    if nominee_type == True:
      num_noms = 10
      if len(nominees) < 10:
        num_noms = len(nominees)
      return numpy.random.choice(nominees, p=probabilities, size=num_noms, replace=False)
    else:
      return numpy.random.choice(nominees, p=probabilities, size=1, replace=False)

  ########## ADMIN ONLY COMMANDS ##########

  # MOVIE NOMINATION
  @commands.hybrid_command(name="nominate_film", description="Nominate for Movie of the Month (ADMIN ONLY)")
  @commands.check(is_admin)
  async def nominate_film(self, ctx):
    """ Nominate members for movie """
    # Get nominees
    nominees = self.nominate(True)

    # Send to embed
    await self.UFS_cmd_nominate(ctx, nominees, True)

  # MUSIC NOMINATION
  @commands.hybrid_command(name="nominate_music", description="Nominate for Music of the Week (ADMIN ONLY)")
  @commands.check(is_admin)
  async def nominate_music(self, ctx):
    """ Nominate members for music"""
    nominees = self.nominate(False)
    await self.UFS_cmd_nominate(ctx, nominees, False)

  # Error if not admin
  @nominate_film.error
  @nominate_music.error
  async def say_error(ctx, error):
    """ Display error to member if they are not an admin"""
    await ctx.send("You must be an admin to use this command", ephemeral=True)

  # Embed Selected MotW/AotW Nominees and Send to Channel
  async def UFS_cmd_nominate(ctx, nominees, nominee_type):
    """ Embed message for nominations and send to server

    ...

    Args:
    - nominees (list[Nominee]): list of nominees
    - nominee_type (bool): The type of nomination, True is movie and False is music
    """
    # Initialize empty pings and embed object
    ping_users = ""
    embed = Embed()

    # Determine author from nominee type
    if nominee_type:
      embed.set_author(name="Movie Nominees")
    else:
      embed.set_author("Music Winner")

    # Embed to Message and Ping
    for i, nominee in enumerate(nominees, 1):
      embed.add_field(name="Nominee #{}".format(i),
                      value=nominee.name(),
                      inline=False)  # Add member
      ping_users += "<@" + nominee.discord_ID() + ">" + " "  # Add to ping

    # Send Winners
    await ctx.send(embed=embed, content=ping_users)
