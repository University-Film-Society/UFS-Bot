# Python Libraries
import random

# External Libraries
from discord.ext import commands


class MiscCog(commands.Cog, name="Misc"):

  def __init__(self, bot):
    self.bot = bot

  # FLIP COMMAND
  @commands.hybrid_command(name="roll", description="Roll an n sided die")
  async def roll(self, ctx, sides: int):
    # Display invalid input
    if sides < 2:
      await ctx.send(
        "What kind of die are you rolling?", ephemeral=True)
    else:
      await ctx.send(
        f"Input: {sides}\nYou rolled a {random.randint(1, sides)}!")
