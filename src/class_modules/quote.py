class Quote:
  _members = None
  _quotes = None
  _date = None
  _film = None
  _year = None

  def __init__(self, members, quotes, date, film=None,year=None):
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