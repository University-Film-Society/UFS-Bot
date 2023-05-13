import random
from discord import File
from discord.ext import commands


class GifCog(commands.Cog, name="Gifs"):
  """
  Summary
  ----------
  - Cog that contains gif-related commands.

  ...

  Attributes
  ----------
  - gif_path (str): filepath to where the gif files are located
  - [movie_name]_path (str): filepaths to gif file or folder
  - bot (Bot): discord bot the cog is attached to
  """

  # UFS discord GIF commands
  def __init__(self, bot):
    """
    Constructs all the necessary attributes for the gif cog object
    
    ...

    Args:
    - gif_path (str): filepath to where the gif files are located
    - [movie_name]_path (str): filepaths to gif file or folder
    - bot (Bot): discord bot the cog is attached to
    """
    self.gif_path = "src/data/gifs/"
    self.M3GAN_path = self.gif_path + "releases/M3GAN/M3GAN"
    self.RRR_path = self.gif_path + "releases/RRR/RRR"
    self.sorcerers_path = self.gif_path + "releases/sorcerers"
    self.minions_path = self.gif_path + "releases/minions/minions"
    self.elvis_path = self.gif_path + "releases/elvis/elvis"
    self.puss_path = self.gif_path + "releases/pussnboots/puss"
    self.pizza_path = self.gif_path + "pizzaTime"
    self.bait_path = self.gif_path + "MadMaxBait"

    self.bot = bot

  ########## 2023 RELATED GIFS ##########
  @commands.hybrid_command(name="gif_m3gan", description="M3GAN (2023)")
  async def gif_m3gan(self, ctx):
    """ M3GAN gif command [2 files in folder]"""
    chance = str(random.randint(1, 2))
    await ctx.send(file=File(self.M3GAN_path + chance + '.gif'))

  
  ########## 2022 RELATED GIFS ##########
  @commands.hybrid_command(name="gif_rrr", description="RRR (2022)")
  async def gif_RRR(self, ctx):
    """ RRR gif command [4 files in folder]"""
    chance = str(random.randint(1, 4))
    await ctx.send(file=File(self.RRR_path + chance + '.gif'))

  
  @commands.hybrid_command(name="gif_sorcerers", description="Wong fortifies your mind")
  async def gif_sorcerers(self, ctx):
    """ Doctor Strange in the Multiverse of Madness gif command [1 file in folder]"""
    await ctx.send(file=File(self.sorcerers_path + '.gif'))

  
  @commands.hybrid_command(name="gif_minions", description="Minions: Rise of Gru (2022)")
  async def gif_minions(self, ctx):
    """ Minions: Rise of Gru gif command [4 files in folder]"""
    chance = str(random.randint(1, 4))
    await ctx.send(file=File(self.minions_path + chance + '.gif'))

  
  @commands.hybrid_command(name="gif_elvis", description="Elvis (2022)")
  async def gif_elvis(self, ctx, everything=None):
    """ Elvis gif command [5 files in folder, 2 options]"""
    if everything is not None:
      await ctx.send(file=File(self.elvis_path + 'Everything.gif'))
    else:
      chance = str(random.randint(1, 4))
      await ctx.send(file=File(self.elvis_path + chance + '.gif'))
  
  @gif_elvis.autocomplete("everything")
  async def gif_elvis_autocompletion(self, ctx, current):
    """ Add autocomplete to elvis 'everything' optional argument"""
    data = []
    data.append(self.app_command.Choice(value="True"))
    return data

  
  @commands.hybrid_command(name="gif_puss", description="Puss in Boots: The Last Wish (2022)")
  async def gif_puss(self, ctx):
    """ Puss in Boots: The Last Wish gif command [5 files in folder]"""
    chance = str(random.randint(1, 5))
    await ctx.send(file=File(self.puss_path + chance + '.gif'))

  
  ########## MISCELLANEOUS ##########
  @commands.hybrid_command(name="gif_pizza", description="Pizza time")
  async def gif_pizza(self, ctx):
    """ Spiderman gif command [1 file]"""
    await ctx.send(file=File(self.pizza_path + '.gif'))

  
  @commands.hybrid_command(name="gif_bait", description="Mad Max calls out bait")
  async def gif_bait(self, ctx):
    """ Mad Max: Fury Road gif command [1 file]"""
    await ctx.send(file=File(self.bait_path + '.gif'))
