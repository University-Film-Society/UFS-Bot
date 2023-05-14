# Python Libraries
import os
import sys

# External Libraries
import discord
from tmdbv3api import TMDb

# Internal libraries
from parsing_modules import csvparser

# Initialize the client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Initialize TMDB
tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

# Initialize keys
BOT_TOKEN = os.environ["BOT_TOKEN"]
UFS_GUILD_ID = os.environ["UFS_GUILD_ID"] # Change this to UFS_GUILD_ID or UFS_TEST_ID

# Initialize quotes
quote_file = "src/data/quotes/quotes.csv"
lbquote_file = "src/data/quotes/lbquotes.csv"

quotes = csvparser.get_quotes(quote_file, True) # List of quotes
lbquotes = csvparser.get_quotes(lbquote_file, False) # List of letterboxd quotes

# If syncing commands to all servers (takes one hour to show)
do_sync = False if len(sys.argv) <= 1 else True