from settings import client, BOT_TOKEN
from server import keep_alive

class DiscordBot:
  def __init__(self):
    pass
  
  def run(self):
    """Run the Discord bot
    """
    # Run the web server
    keep_alive()
    
    # Run the bot with the bot token
    client.run(BOT_TOKEN)
    
