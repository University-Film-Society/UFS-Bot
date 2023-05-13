import csv
import Quote
from collections import defaultdict

def def_value():
  return 0

def get_quotes(filename):
  quotes = [] # Initialize list of empty quotes

  # ADMIN
  lbquote_counts = defaultdict(def_value)
  lbfilm_counts = defaultdict(def_value)
  count = 1
  
  with open(filename) as file:
    csv_reader = csv.reader(file, delimiter = ';')
    for row in csv_reader:
      if row[0] == "Members": continue
      if filename == "quotes.csv": # Regular quote
          
        currQuote = Quote.Quote(row[0], row[1].replace("$", "\n"), row[2])
        quotes.append(currQuote)
      else: # Letterboxd quote

        # ADMIN: Get Member LB Quote Count
        lbquote_counts[row[0]] = lbquote_counts[row[0]] + 1
        lbfilm_counts[row[3]] = lbfilm_counts[row[3]] + 1
        # ADMIN: Test Incorrect Quote Locations
        print(count)
        count += 1
        
        currQuote = Quote.Quote(row[0], row[1].replace("$", "\n"), row[2], row[3], row[4])
        quotes.append(currQuote)

  lbquote_counts = {k: v for k, v in sorted(lbquote_counts.items(), reverse=True, key=lambda item: item[1])}

  """
  print("\n\nLB QUOTE COUNT")
  total = 0
  for key, value in lbquote_counts.items():
    print(key + ": " + str(value))
    total += value
  print("\nTOTAL: " + str(total))

  lbfilm_counts = {k: v for k, v in sorted(lbfilm_counts.items(), reverse=True, key=lambda item: item[1])}
  print("\n\nLB FILM COUNT")
  total = 0
  for key, value in lbfilm_counts.items():
    print(key + ": " + str(value))
    total += 1
  print("\nTOTAL: " + str(total))
  """

  return quotes