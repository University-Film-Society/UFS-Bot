import copy
import random

class BotFunctions:
  # Get Random UFS Member Quote Object from CSV File (handles either quotes or letterboxd quotes)
  def get_quote(quote_type):
    global quotes_queue  # Clarify reference to quotes queue
    global quotes
    global lbquotes_queue  # Clarify reference to lbquotes queue
    global lbquotes
    curr_queue = []
    # Get correct queue type, reset queue if necessary
    if quote_type == True:  # Regular quote
      if len(quotes_queue) == 0:
        quotes_queue = copy.deepcopy(quotes)
      curr_queue = quotes_queue
    else:  # Letterboxd quote
      if len(lbquotes_queue) == 0:
        lbquotes_queue = copy.deepcopy(lbquotes)
      curr_queue = lbquotes_queue
  
    # Generate a random index, return the quote at the index
    if len(curr_queue) >= 2:  # If more than one quote in queue
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
  