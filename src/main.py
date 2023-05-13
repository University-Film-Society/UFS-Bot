# Code is divided into multiple files for ease of readability and understanding
from bot import DiscordBot

if __name__ == "__main__":
  bot = DiscordBot()
  bot.run()

# Note: If bot breaks, run 'kill 1' in shell and restartpingerdiscord.utils.get(client.users, name=name_only, discriminator=discriminator_only)