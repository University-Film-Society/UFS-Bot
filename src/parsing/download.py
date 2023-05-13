import csv
from UFSNominee import Nominee

def get_nominees(filename):
    nominees = []
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')
        row_count = 0
        for row in csv_reader:
            if row_count != 0:
                if row[0] == '' : break
                if row[3] == 'A' or row[3] == 'B' or row[3] == 'C':
                    curNom = Nominee.Nominee(row[0], row[1], row[2], row[3])
                    nominees.append(curNom)
            row_count += 1
        
    return nominees