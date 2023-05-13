# Python Libraries
import random

# External Libraries
from discord.ext import commands


class MiscCog(commands.Cog, name="Misc"):
  """
  Summary
  ----------
  - Cog that contains miscellaneous commands.

  ...

  Attributes
  ----------
  - bot (Bot): discord bot the cog is attached to
  """

  def __init__(self, bot):
    """
    Constructs all the necessary attributes for the misc cog object
    
    ...

    Args:
    - bot (Bot): discord bot the cog is attached to
    """
    self.bot = bot

  # FLIP COMMAND
  @commands.hybrid_command(name="roll", description="Roll an n sided die")
  async def roll(self, ctx, sides: int):
    """Roll an n-sided die and send the output to the server
    
    ...

    Args:
    - sides (int): The number of sides on the die
    """
    # Display invalid input
    if sides < 2:
      await ctx.send("What kind of die are you rolling?", ephemeral=True)
    else:
      await ctx.send(
        f"Input: {sides}\nYou rolled a {random.randint(1, sides)}!")
