import csv
from class_modules.quote import Quote

def def_value():
  return 0

def get_quotes(filename, file_type):
  quotes = [] # Initialize list of empty quotes
  
  with open(filename) as file:
    csv_reader = csv.reader(file, delimiter = ';')
    for row in csv_reader:
      if row[0] == "Members": continue
      if file_type: # Regular quote
        currQuote = Quote(row[0], row[1].replace("$", "\n"), row[2])
        quotes.append(currQuote)
      else: # Letterboxd quote
        currQuote = Quote(row[0], row[1].replace("$", "\n"), row[2], row[3], row[4])
        quotes.append(currQuote)

  return quotes