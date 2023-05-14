# Python Libraries
import random
import copy

# External Libraries
from class_modules.movie import Movie  # Modification of tmdbv3api Movie
from discord import Embed
from discord.ext import commands

# Internal Files
from settings import quotes, lbquotes  


class QuoteCog(commands.Cog, name="Quotes"):
  """
  Summary
  ----------
  - Cog that contains quote-related commands.

  ...

  Attributes
  ----------
  - quotes_queue (list[Quote]): copy of original list of quotes
  - lbquotes_queue (list[Quote]): copy of original list of lbquotes
  - bot (Bot): discord bot the cog is attached to
  """

  def __init__(self, bot):
    """
    Constructs all the necessary attributes for the nominate cog object
    
    ...

    Args:
    - quote_file (str): filepath to the quotes .csv
    - lbquote_file (str): filepath to the lbquote_file .csv
    - quotes (list[Quote]): original list of quote objects
    - lbquotes (list[Quote]): original list of letterboxd quote objects
    - quotes_queue (list[Quote]): copy of quotes
    - lbquotes_queue (list[Quote]): copy of lbquotes
    - bot (Bot): discord bot the cog is attached to
    """
    self.quotes_queue = copy.deepcopy(quotes)
    self.lbquotes_queue = copy.deepcopy(lbquotes)

    self.bot = bot

  @staticmethod
  def get_random_quote(quote_queue):
    """ Get random UFS member quote object from a list
    
    ...

    Args:
    - quote_queue (list) : list of quotes

    Returns:
    - quote: quote object
    - int: index of quote object
    """
    
    # Generate a random index, return the quote at the index
    if len(quote_queue) >= 2:  # If more than one quote in queue
      randomQuoteIndex = random.randrange(0, len(quote_queue) - 1)
    else:
      randomQuoteIndex = 0

    # Return random quote and its index
    quoteToReturn = quote_queue[randomQuoteIndex]
    return quoteToReturn, randomQuoteIndex
    
    
  def get_quote(self, quote_type):
    """ Get random UFS member quote object and update the corresponding list of quotes
    
    ...

    Args:
    - quote_type (bool): The type of quote, True is regular quote and False is letterboxd quote

    Returns:
    - quote: quote object
    """
    curr_queue = []
    # Get correct queue type, reset queue if necessary
    if quote_type == True:  # Regular quote
      if len(self.quotes_queue) == 0:
        self.quotes_queue = copy.deepcopy(quotes)
      curr_queue = self.quotes_queue
    else:  # Letterboxd quote
      if len(self.lbquotes_queue) == 0:
        self.lbquotes_queue = copy.deepcopy(lbquotes)
      curr_queue = self.lbquotes_queue

    # Generate a random index, return the quote at the index
    quoteToReturn, randomQuoteIndex = self.get_random_quote(curr_queue)

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
    """ Random quote from UFS member """
    # Gets a Quote object
    quote = self.get_quote(True)

    # Send to Embed
    await self.UFS_cmd_quote(ctx, quote)

  # LETTERBOXD QUOTE COMMAND
  @commands.hybrid_command(
    name="lbquote", description="Random letterboxd review from a UFS member")
  async def lbquote(self, ctx):
    """ Random letterboxd quote from UFS member """
    # Get Quote Object
    lbquote = self.get_quote(False)

    # Get Poster from TMDB
    search = Movie().search(lbquote.film(), year=lbquote.year())
    poster = "https://image.tmdb.org/t/p/original{}".format(
      search[0].poster_path)

    # Send to Embed
    await self.UFS_cmd_lbquote(ctx, lbquote, poster)

  # Embed Quote and Send to Channel
  async def UFS_cmd_quote(self, ctx, quote):
    """ Embed quote and send to server """
    # Embed Quote
    quote_embed = Embed() # Embed object
    quote_embed.set_author(name=quote.members()) # Add members as author
    quote_embed.add_field(name="\u200b", value=quote.quotes(), inline=False) # Add quote
    quote_embed.add_field(name="\u200b", value=quote.date(), inline=False) # Add date
    
    # Send Quote
    await ctx.send(embed=quote_embed)

  # Embed Letterboxd Quote and Send to Channel
  async def UFS_cmd_lbquote(self, ctx, lbquote, poster):
    """ Embed letterboxd quote and send to server"""
    # Embed Quote
    lbquote_embed = Embed() # Embed object
    lbquote_embed.set_thumbnail(url=poster) # Add poster jpeg
    lbquote_embed.set_author(name=lbquote.film() + " (" + lbquote.year() + ")") # Add film name and year as author
    lbquote_embed.add_field(name="\u200b", value=lbquote.members(), inline=True) # Add members
    lbquote_embed.add_field(name="\u200b", value=lbquote.date(), inline=False) # Add date
    lbquote_embed.add_field(name="\u200b", value=lbquote.quotes(), inline=False) # Add quote

    # Send Quote
    await ctx.send(embed=lbquote_embed)