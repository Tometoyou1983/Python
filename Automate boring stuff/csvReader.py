# python 3
# sample program to read, copy, write csv files using csv module.

import os, csv

os.system('cls')
csvFile = open('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/example.csv')
csvRead = csv.reader(csvFile)
csvWrite  =open('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/exampleWrite.csv', 'w', newline='')
for row in csvRead:
    print(f'Row {csvRead.line_num}# {row}')
    csv.writer(csvWrite).writerow(row)

