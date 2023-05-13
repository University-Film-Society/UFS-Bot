########################## INCLUDES ###########################
# Python Libraries
import os
import random
import copy
# External Libraries
import discord
from discord import app_commands
from tmdbv3api import TMDb
from Movie import Movie # Modification of tmdbv3api Movie
# My Files
from keep_alive import keep_alive
import csvparser
from UFSNominee import NomineeSelector
####################### END OF INCLUDES #######################


########################## GLOBALS ############################
# Initialize the client
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Initialize TMDB
tmdb = TMDb()
tmdb.api_key = os.environ['TMDB_API_KEY']

# Global variables to manage quotes
quotes = csvparser.get_quotes('quotes.csv')
lbquotes = csvparser.get_quotes('lbquotes.csv')
quotes_queue = copy.deepcopy(quotes)
lbquotes_queue = copy.deepcopy(lbquotes)
####################### END OF GLOBALS ########################


######################## BOT FUNCTIONS ########################
# Get Random UFS Member Quote Object from CSV File (handles either quotes or letterboxd quotes)
def get_quote(quote_type):
  global quotes_queue # Clarify reference to quotes queue
  global quotes
  global lbquotes_queue # Clarify reference to lbquotes queue
  global lbquotes
  curr_queue = []
  # Get correct queue type, reset queue if necessary
  if quote_type == True: # Regular quote
    if len(quotes_queue) == 0:
      quotes_queue = copy.deepcopy(quotes)
    curr_queue = quotes_queue
  else: # Letterboxd quote
    if len(lbquotes_queue) == 0:
      lbquotes_queue = copy.deepcopy(lbquotes)
    curr_queue = lbquotes_queue

  # Generate a random index, return the quote at the index
  if len(curr_queue) >= 2: # If more than one quote in queue
    randomQuoteIndex = random.randrange(0, len(curr_queue) - 1)
  else:
    randomQuoteIndex = 0
  quoteToReturn = curr_queue[randomQuoteIndex]

  # Delete corresponding quote from queue
  if quote_type:
    del quotes_queue[randomQuoteIndex]
  else:
    del lbquotes_queue[randomQuoteIndex]
  
  return quoteToReturn

# Check if the user is allowed to use an admin-only slash command
def is_admin(interaction):
  if "exec" in [role.name for role in interaction.user.roles]:
    return True
  return False
  
##################### END OF BOT FUNCTIONS ####################

########################## BOT EMBEDS #########################
	
# Embed Quote and Send to Channel
async def UFS_cmd_quote(interaction):
  quoter = get_quote(True) # Gets a Quote object

  # Embed Quote
  quote_embed = discord.Embed()
  quote_embed.set_author(name=quoter.members())
  quote_embed.add_field(name="\u200b", value=quoter.quotes(), inline=False)
  quote_embed.add_field(name="\u200b", value=quoter.date(), inline=False)
  
  await interaction.response.send_message(embed=quote_embed)
	

# Embed Letterboxd Quote and Send to Channel
async def UFS_cmd_lbquote(interaction):
  # Gets Quote object
  lbquote = get_quote(False)
  
  # Get Poster from TMDB
  search = Movie().search(lbquote.film(), year=lbquote.year())
  poster_jpeg = "https://image.tmdb.org/t/p/original{}".format(search[0].poster_path)
  
  # Embed Quote
  lbquote_embed = discord.Embed()
  lbquote_embed.set_thumbnail(url=poster_jpeg)
  lbquote_embed.set_author(name=lbquote.film() + " (" + lbquote.year() + ")")
  lbquote_embed.add_field(name="\u200b", value=lbquote.members(), inline=True)
  lbquote_embed.add_field(name="\u200b", value=lbquote.date(), inline=False)
  lbquote_embed.add_field(name="\u200b", value=lbquote.quotes(), inline=False)
  
  await interaction.response.send_message(embed=lbquote_embed)

# Embed Selected MotW/AotW Nominees and Send to Channel
async def UFS_cmd_nominate(interaction, nominee_type):
  # Array of Nominees
  nominees = NomineeSelector.nominate(nominee_type) 
  embed = None
  ping_users = ""
  
  # Movie of the Week Embed
  embed = discord.Embed()
  if nominee_type == 1:
    embed.set_author(name="MOTM Nominees")
  
  # Embed to Message and Ping
  for i, nominee in enumerate(nominees, 1):
    if nominee_type == 1:
      embed.add_field(name="Nominee #{}".format(i), value=nominee.name(), inline=False)
    else:
      embed.add_field(name="Music Winner", value=nominee.name(), inline=False)
    ping_users += "<@"+nominee.discord_ID()+">"+" "
  await interaction.response.send_message(embed=embed, content=ping_users)

async def UFS_cmd_roll(interaction, sides):
  if (sides < 2):
    await interaction.response.send_message("What kind of die are you rolling?", ephemeral=True)
  else:
    n = random.randint(1, sides)
    await interaction.response.send_message(f"Input: {sides}\nYou rolled a {n}!")
##################### END OF BOT EMBEDS #######################

  
######################### BOT EVENTS ##########################
# Event if bot is ready
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
  await tree.sync(guild=discord.Object(id=UFS_GUILD_ID))
###################### END OF BOT EVENTS ######################

  
######################## BOT COMMANDS #########################
# QUOTE
@tree.command(name="quote", description="Random out-of-context quote from a UFS member", guild=discord.Object(id=UFS_GUILD_ID))
async def quote(interaction):
  await UFS_cmd_quote(interaction)

# LETTERBOXD QUOTE
@tree.command(name="lbquote", description="Random letterboxd review from a UFS member", guild=discord.Object(id=UFS_GUILD_ID))
async def lbquote(interaction):
  await UFS_cmd_lbquote(interaction)

# MOVIE OF THE MONTH (ADMIN-ONLY)
@tree.command(name="nominatefilm", description="Nominate for Movie of the Month (ADMIN ONLY)", guild=discord.Object(id=UFS_GUILD_ID))
@app_commands.check(is_admin)
async def nominatefilm(interaction):
  await UFS_cmd_nominate(interaction, True)
  
# MUSIC OF THE WEEK (ADMIN-ONLY)
@tree.command(name="nominatemusic", description="Nominate for Music of the Week (ADMIN ONLY)", guild=discord.Object(id=UFS_GUILD_ID))
@app_commands.check(is_admin)
async def nominatemusic(interaction):
  await UFS_cmd_nominate(interaction, False)

@nominatefilm.error
@nominatemusic.error
async def say_error(interaction, error):
  await interaction.response.send_message("You must be an admin to use this command", ephemeral=True)

# FLIP
@tree.command(name="roll", description="Roll a n sided die", guild=discord.Object(id=UFS_GUILD_ID))
async def roll(interaction, sides: int):
  await UFS_cmd_roll(interaction, sides)

##################### END OF BOT COMMANDS #####################


######################## GIF COMMANDS #########################
# UFS discord GIF commands

##### 2023 RELATED GIFS #####
@tree.command(name="m3gan", description="M3GAN (2023)", guild=discord.Object(id=UFS_GUILD_ID))
async def m3gan(interaction):
  chance = str(random.randint(1,2))
  await interaction.response.send_message(file=discord.File('Gifs/Releases/M3GAN/M3GAN' + chance + '.gif'))

##### 2022 RELATED GIFS #####
@tree.command(name="rrr", description="RRR (2022)", guild=discord.Object(id=UFS_GUILD_ID))
async def RRR(interaction):
  chance = str(random.randint(1,4))
  await interaction.response.send_message(file=discord.File('Gifs/Releases/RRR/RRR' + chance + '.gif'))

@tree.command(name="sorcerers", description="Wong fortifies your mind", guild=discord.Object(id=UFS_GUILD_ID))
async def sorcerers(interaction):
  await interaction.response.send_message(file=discord.File('Gifs/Releases/sorcerers.gif'))

@tree.command(name="minions", description="Minions: Rise of Gru (2022)", guild=discord.Object(id=UFS_GUILD_ID))
async def minions(interaction):
  chance = str(random.randint(1,4))
  await interaction.response.send_message(file=discord.File('Gifs/Releases/minions/minions' + chance + '.gif'))

@tree.command(name="elvis", description="Elvis (2022)", guild=discord.Object(id=UFS_GUILD_ID))
async def elvis(interaction):
  chance = str(random.randint(1,4))
  await interaction.response.send_message(file=discord.File('Gifs/Releases/elvis/elvis' + chance + '.gif'))

@tree.command(name="everything", description="It has everything to do with us", guild=discord.Object(id=UFS_GUILD_ID))
async def everything(interaction):
  await interaction.response.send_message(file=discord.File('Gifs/Releases/elvis/elvisEverything.gif'))

@tree.command(name="puss", description="Puss in Boots: The Last Wish (2022)", guild=discord.Object(id=UFS_GUILD_ID))
async def puss(interaction):
  chance = str(random.randint(1,5))
  await interaction.response.send_message(file=discord.File('Gifs/Releases/pussnboots/puss' + chance + '.gif'))

##### REACTION GIFS #####
@tree.command(name="pizza", description="Pizza time", guild=discord.Object(id="UFS_GUILD_ID"))
async def pizza(interaction):
  await interaction.response.send_message(file=discord.File('Gifs/pizzaTime.gif'))

@tree.command(name="bait", description="Mad Max calls out bait", guild=discord.Object(id=os.environ["UFS_GUILD_ID"]))
async def bait(interaction):
  await interaction.response.send_message(file=discord.File('Gifs/MadMaxBait.gif'))

##################### END OF GIF COMMANDS #####################


# Run web server
keep_alive()
# Run the bot with the bot token
client.run(os.environ['BOT_TOKEN'])

# Note: If bot breaks, run 'kill 1' in shell and restartpingerdiscord.utils.get(client.users, name=name_only, discriminator=discriminator_only)