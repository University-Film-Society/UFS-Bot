from UFSNominee import Nominee
from UFSNominee import Download

import numpy

def get_probabilities(nominees, total):
    weights = []
    for nominee in nominees:
        if nominee.check() == 'A':
            # Not previously selected prioritized
            weights.append(50)
            # Previously selected
        if nominee.check() == 'B' or nominee.check() == 'C':
            weights.append(10)

    probabilities = []
    total = sum(weights)
    for weight in weights:
        probabilities.append(weight/total)
    
    return probabilities

def nominate(nominee_type):
    week_type = "Movie of the Month.csv" if nominee_type == True else "Music of the Week.csv"

    nominees = Download.get_nominees("UFSNominee/" + week_type)
    probabilities = get_probabilities(nominees, len(nominees))

    if nominee_type == 1:
      num_noms = 10
      if len(nominees) < 10:
        num_noms = len(nominees)
      return numpy.random.choice(nominees, p=probabilities, size=num_noms, replace=False)
    else:   
      return numpy.random.choice(nominees, p=probabilities, size=1, replace=False)