class Nominee:
  """
  Summary
  ----------
  - UFS member nominee for either movie or music nomination.
  
  ...

  Attributes
  ----------
  - name (str): name of the member
  - discord_name (str): discord username for the member
  - discord_ID (str): discord ID for the member
  - check (str): nomination type (A, B, C, 0-3)
  """

  def __init__(self, name, discord_name, discord_ID, check):
    """
    Constructs all the necessary attributes for the nominee object
    
    ...

    Args:
    - name (str): name of the member
    - discord_name (str): discord username for the member
    - discord_ID (str): discord ID for the member
    - check (str): the nomination type (A, B, C, 0-3)
    """

    # Check for missing parameter first
    if name == None or discord_name == None or check == None or discord_ID == None:
      raise Exception("Missing constructor parameter")
    self._name = name
    self._discord_name = discord_name
    self._discord_ID = discord_ID
    self._check = check

  def name(self):
    return self._name

  def discord_name(self):
    return self._discord_name

  def discord_ID(self):
    return self._discord_ID

  def check(self):
    return self._check