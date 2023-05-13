# Python Libraries
import os
import sys

# External Libraries
import discord
from tmdbv3api import TMDb

# Initialize the client
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Initialize TMDB
tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

# Initialize keys
BOT_TOKEN = os.environ["BOT_TOKEN"]
UFS_GUILD_ID = os.environ["UFS_TEST_ID"]

# If syncing commands to all servers (takes one hour to show)
do_sync = False if len(sys.argv) <= 1 else True