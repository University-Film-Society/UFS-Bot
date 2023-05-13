# External
from discord.ext.commands import Bot
from discord import Game, Intents

# Locals
from cogs.nominate_cog import NominateCog
from cogs.gif_cog import GifCog
from cogs.quote_cog import QuoteCog
from cogs.misc_cog import MiscCog


class DiscordBot(Bot):
  # Event if bot is ready
  async def on_ready(self):
    # Add cogs (groups of commands)
    await self.add_cog(NominateCog(self))
    await self.add_cog(GifCog(self))
    await self.add_cog(QuoteCog(self))
    await self.add_cog(MiscCog(self))

    # Set bot activity
    activity = Game(
      name= "I see you're looking at my fingers, lad. Well let me tell you the story of FART and BOMB...",
      type=1)
    await self.change_presence(activity=activity)

    # Inform dev of successful login
    print(f"We have logged in as {self.user}")

  def __init__(self, command_prefix, help_command=None, description=None, **options):
    super().__init__(command_prefix,
                     #help_command=help_command,
                     description=description,
                     **options,
                     intents=Intents.all())