#python 3
# remove headers in the csv.

import os, csv
os.system('cls')

newDir = 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/headerRemoved/'
try:
    os.listdir(newDir)
except:
    os.mkdir('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/headerRemoved/')

# Loop through every file in the current working directory.
fileDirectory = 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/removeCsvHeader/'
for csvFileName in os.listdir(fileDirectory):
    if not csvFileName.endswith('.csv'):
        continue
    print('Removing the header from ' + csvFileName + '.....')
    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj  = open(fileDirectory + csvFileName)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join(newDir, csvFileName), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()