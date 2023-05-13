# Code is divided into multiple files for ease of readability and understanding
from settings import BOT_TOKEN
from class_modules.bot import DiscordBot
from server import keep_alive

if __name__ == "__main__":
  # Run the web server
  keep_alive()
  
  # Run the bot with the bot token
  discord_bot = DiscordBot(
    command_prefix="/",
    #help_command=DefaultHelpCommand(),
    description="UFS Discord Bot",
    case_insensitive=True,
  )
  
  discord_bot.run(BOT_TOKEN)
  

# Note: If bot breaks, run 'kill 1' in shell and restartpingerdiscord.utils.get(client.users, name=name_only, discriminator=discriminator_only)