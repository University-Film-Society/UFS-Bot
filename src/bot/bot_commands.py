# Python Libraries
import random

# External Libraries
from Movie import Movie  # Modification of tmdbv3api Movie

# Globals and Internal Files
from settings import discord, tree, app_commands, UFS_GUILD_ID

# Superclass
from bot_embeds import BotEmbeds
from bot_functions import BotFunctions
from bot_gif_commands import BotGifs
from nominee_selector import NomineeSelector


class BotCommands(BotEmbeds, BotFunctions, BotGifs, NomineeSelector):
  # QUOTE
  @tree.command(name="quote",
                description="Random out-of-context quote from a UFS member",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def quote(self, interaction):
    # Gets a Quote object
    quoter = self.get_quote(True)

    # Send to Embed
    await self.UFS_cmd_quote(interaction, quoter)

  # LETTERBOXD QUOTE
  @tree.command(name="lbquote",
                description="Random letterboxd review from a UFS member",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def lbquote(self, interaction):
    # Get Quote Object
    lbquote = self.get_quote(False)

    # Get Poster from TMDB
    search = Movie().search(lbquote.film(), year=lbquote.year())
    poster = "https://image.tmdb.org/t/p/original{}".format(
      search[0].poster_path)
    # Send to Embed
    await self.UFS_cmd_lbquote(interaction, lbquote, poster)

  # MOVIE OF THE MONTH (ADMIN-ONLY)
  @tree.command(name="nominatefilm",
                description="Nominate for Movie of the Month (ADMIN ONLY)",
                guild=discord.Object(id=UFS_GUILD_ID))
  @app_commands.check(BotFunctions.is_admin)
  async def nominatefilm(self, interaction):
    # Get nominees
    nominees = self.nominate(True)
    await self.UFS_cmd_nominate(interaction, nominees, True)

  # MUSIC OF THE WEEK (ADMIN-ONLY)
  @tree.command(name="nominatemusic",
                description="Nominate for Music of the Week (ADMIN ONLY)",
                guild=discord.Object(id=UFS_GUILD_ID))
  @app_commands.check(BotFunctions.is_admin)
  async def nominatemusic(self, interaction):
    nominees = self.nominate(False)
    await self.UFS_cmd_nominate(interaction, nominees, False)

  @nominatefilm.error
  @nominatemusic.error
  async def say_error(interaction, error):
    await interaction.response.send_message(
      "You must be an admin to use this command", ephemeral=True)

  # FLIP
  @tree.command(name="roll",
                description="Roll a n sided die",
                guild=discord.Object(id=UFS_GUILD_ID))
  async def roll(self, interaction, sides: int):
    n = None if sides < 2 else random.randint(1, sides)
    await self.UFS_cmd_roll(interaction, sides, n)
