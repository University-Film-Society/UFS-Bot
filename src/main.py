# External
from discord.ext.commands import DefaultHelpCommand

# Internal
from settings import BOT_TOKEN
from class_modules.bot import DiscordBot
from server import keep_alive

if __name__ == "__main__":
  # Run the web server
  keep_alive()
  
  # Initialize the discord bot
  discord_bot = DiscordBot(
    command_prefix="/",
    help_command=DefaultHelpCommand(),
    description="UFS Discord Bot",
    case_insensitive=True,
  )

  # Run the discord bot with the bot token
  discord_bot.run(BOT_TOKEN)
  

# Note: If bot breaks, run 'kill 1' in shell and restartpingerdiscord.utils.get(client.users, name=name_only, discriminator=discriminator_only)