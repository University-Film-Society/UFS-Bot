########################## INCLUDES ###########################
# Python Libraries
import os
import copy
# External Libraries
import discord
from discord import app_commands
from tmdbv3api import TMDb

# My Files
import csvparser
####################### END OF INCLUDES #######################

# Initialize the client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Initialize TMDB
tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

# Initialize keys
BOT_TOKEN = os.environ["BOT_TOKEN"]
UFS_GUILD_ID = os.environ["TEST_GUILD_ID"]

# Global variables to manage quotes
quotes = csvparser.get_quotes('quotes.csv')
lbquotes = csvparser.get_quotes('lbquotes.csv')
quotes_queue = copy.deepcopy(quotes)
lbquotes_queue = copy.deepcopy(lbquotes)