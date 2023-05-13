class Quote:
  """
  Summary
  ----------
  - UFS member quote for either real quote or letterboxd review.
  
  ...

  Attributes
  ----------
  - members (str): name of the members
  - quotes (str): quote body
  - date (str): date of the quote
  - film (str): name of the film if a letterboxd review
  - year (str): year of film release if a letterboxd review
  """
  _members = None
  _quotes = None
  _date = None
  _film = None
  _year = None

  def __init__(self, members, quotes, date, film=None,year=None):
    """
    Constructs all the necessary attributes for the quote object
    
    ...

    Args:
    - members (str): name of the members
    - quotes (str): quote body
    - date (str): date of the quote
    - film (str): name of the film if a letterboxd review
    - year (str): year of film release if a letterboxd review
    """

    # Check for missing parameter first
    if(members == "" or quotes == "" or date == "" or film == "" or year==""):
      raise Exception("Missing constructor parameter")
    self._members = members
    self._quotes = quotes
    self._date = date
    self._film = film
    self._year = year

  def members(self): return self._members
  def quotes(self): return self._quotes
  def date(self): return self._date
  def film(self): return self._film
  def year(self): return self._year