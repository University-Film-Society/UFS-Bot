# External Libraries
from discord.ext.commands import Bot, DefaultHelpCommand
from discord import Activity, ActivityType, Intents, Object

# Internal Files
from settings import do_sync, UFS_GUILD_ID, lbquotes
from cogs.nominate_cog import NominateCog
from cogs.gif_cog import GifCog
from cogs.quote_cog import QuoteCog
from cogs.misc_cog import MiscCog


class DiscordBot(Bot):
  """
  Summary
  ----------
  - Main Bot class to run.
  """

  async def on_ready(self):
    """Event that executes when the bot first starts up
    - Instantiate and add cogs (grouped commands) to the bot
    - Set the bot activity
    - Notify developer of successful login
    """
    # Add cogs (groups of commands)
    await self.add_cog(NominateCog(self))
    await self.add_cog(GifCog(self))
    await self.add_cog(QuoteCog(self))
    await self.add_cog(MiscCog(self))

    # Set bot activity to watching a random movie
    movie, _ = QuoteCog.get_random_quote(lbquotes)
    activity = Activity(type=ActivityType.watching, name=movie.film())
    await self.change_presence(activity=activity)

    if (do_sync):
      print("\nSyncing...", end= " ")
      await self.tree.sync(guild=Object(id=UFS_GUILD_ID))
      print("synced.")

    # Inform dev of successful login
    print(f"\nWe have logged in as {self.user}")

  
  def __init__(self, command_prefix="/", help_command=DefaultHelpCommand(), description="UFS Discord Bot", **options):
    """Default constructor
    
    ...

    Args:
    - command_prefix (str): the string that determines what is considered a command
    - help_command (function): help command that shows all commands in the bot
    - description (str): description of the bot
    - **options: Keyword arguments
    """
    super().__init__(command_prefix, help_command=help_command,
                     description=description, **options,
                     intents=Intents.all())
