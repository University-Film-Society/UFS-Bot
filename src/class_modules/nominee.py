class Nominee:
    _name = None
    _discord_name = None
    _discord_ID = None
    _check = None

    
    def __init__(self, name, discord_name, discord_ID, check):
        if(name == None or discord_name == None or check == None or discord_ID == None):
            raise Exception("Missing constructor parameter")
        self._name = name
        self._discord_name = discord_name
        self._discord_ID = discord_ID
        self._check = check


    def name(self): return self._name
    def discord_name(self): return self._discord_name
    def discord_ID(self): return self._discord_ID
    def check(self): return self._check
