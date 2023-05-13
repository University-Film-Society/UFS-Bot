# Python Libraries
import copy
import random

# External Libraries
from class_modules.movie import Movie  # Modification of tmdbv3api Movie
from discord import Embed
from discord.ext import commands

# Internal Files
import parsing_modules.csvparser as csvparser


class QuoteCog(commands.Cog, name="Quotes"):

  def __init__(self, bot):
    self.quote_file = "src/data/quotes/quotes.csv"
    self.lbquote_file = "src/data/quotes/lbquotes.csv"

    self.quotes = csvparser.get_quotes(self.quote_file, True)
    self.lbquotes = csvparser.get_quotes(self.lbquote_file, False)

    self.quotes_queue = copy.deepcopy(self.quotes)
    self.lbquotes_queue = copy.deepcopy(self.lbquotes)

    self.bot = bot

  # Get Random UFS Member Quote Object from CSV File (handles either quotes or letterboxd quotes)
  def get_quote(self, quote_type):
    curr_queue = []
    # Get correct queue type, reset queue if necessary
    if quote_type == True:  # Regular quote
      if len(self.quotes_queue) == 0:
        self.quotes_queue = copy.deepcopy(self.quotes)
      curr_queue = self.quotes_queue
    else:  # Letterboxd quote
      if len(self.lbquotes_queue) == 0:
        self.lbquotes_queue = copy.deepcopy(self.lbquotes)
      curr_queue = self.lbquotes_queue

    # Generate a random index, return the quote at the index
    if len(curr_queue) >= 2:  # If more than one quote in queue
      randomQuoteIndex = random.randrange(0, len(curr_queue) - 1)
    else:
      randomQuoteIndex = 0
    quoteToReturn = curr_queue[randomQuoteIndex]

    # Delete corresponding quote from queue
    if quote_type:
      del self.quotes_queue[randomQuoteIndex]
    else:
      del self.lbquotes_queue[randomQuoteIndex]

    return quoteToReturn

  # QUOTE COMMAND
  @commands.hybrid_command(
    name="quote", description="Random out-of-context quote from a UFS member")
  async def quote(self, ctx):
    # Gets a Quote object
    quote = self.get_quote(True)

    # Send to Embed
    await self.UFS_cmd_quote(ctx, quote)

  # LETTERBOXD QUOTE COMMAND
  @commands.hybrid_command(
    name="lbquote", description="Random letterboxd review from a UFS member")
  async def lbquote(self, ctx):
    # Get Quote Object
    lbquote = self.get_quote(False)

    # Get Poster from TMDB
    search = Movie().search(lbquote.film(), year=lbquote.year())
    poster = "https://image.tmdb.org/t/p/original{}".format(
      search[0].poster_path)

    # Send to Embed
    await self.UFS_cmd_lbquote(ctx, lbquote, poster)

  # Embed Quote and Send to Channel
  async def UFS_cmd_quote(ctx, quote):
    # Embed Quote
    quote_embed = Embed() # Embed object
    quote_embed.set_author(name=quote.members()) # Add members as author
    quote_embed.add_field(name="\u200b", value=quote.quotes(), inline=False) # Add quote
    quote_embed.add_field(name="\u200b", value=quote.date(), inline=False) # Add date
    
    # Send Quote
    await ctx.send(embed=quote_embed)

  # Embed Letterboxd Quote and Send to Channel
  async def UFS_cmd_lbquote(ctx, lbquote, poster):
    # Embed Quote
    lbquote_embed = Embed() # Embed object
    lbquote_embed.set_thumbnail(url=poster) # Add poster jpeg
    lbquote_embed.set_author(name=lbquote.film() + " (" + lbquote.year() + ")") # Add film name and year as author
    lbquote_embed.add_field(name="\u200b", value=lbquote.members(), inline=True) # Add members
    lbquote_embed.add_field(name="\u200b", value=lbquote.date(), inline=False) # Add date
    lbquote_embed.add_field(name="\u200b", value=lbquote.quotes(), inline=False) # Add quote

    # Send Quote
    await ctx.send(embed=lbquote_embed)
