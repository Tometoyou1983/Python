# python 3
# program to rename files with american style dates to european style dates 
# American style date is MM-DD-YYYY
# European style date is DD-MM-YYYY

import os, shutil, re, time, datetime 
os.system('cls')

# creating Regex for finding American style dates
datePattern = re.compile(r"""(^(.*?) # all text before the date
       (((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d))                   # four digits for the year
       (.*?)$)                          # all text after the date
     """, re.VERBOSE)

# capture the directory user wants to look in 
def renameFiles(files_Dct):
    print("Renaming files in the respective directories...")
    for keys in files_Dct:
        oldDate = re.findall(datePattern, keys)
        if datetime.datetime.strptime(oldDate[0][2], "%m-%d-%Y"):
           newDate = datetime.datetime.strptime(oldDate[0][2], "%m-%d-%Y").strftime("%d-%m-%Y")
           newfilename = files_Dct[keys] + (oldDate[0][0].replace(oldDate[0][2], newDate))
           oldfilepath = files_Dct[keys] + keys
           shutil.move(oldfilepath,newfilename)
    print("Files have been renamed with new date format.Please review")            
def createFiles(files_Dct):
    print("Creating new files in the respective directories...")
    for keys in files_Dct:
        oldDate = re.findall(datePattern, keys)
        if datetime.datetime.strptime(oldDate[0][2], "%m-%d-%Y"):
            newDate = datetime.datetime.strptime(oldDate[0][2], "%m-%d-%Y").strftime("%d-%m-%Y")
            newfilename = files_Dct[keys] + (oldDate[0][0].replace(oldDate[0][2], newDate))
            oldfilepath = files_Dct[keys] + keys
            shutil.copy(oldfilepath,newfilename)

    print("Files have been created with new date format.Please review")
filesinDir = {}
print('Program to rename files with American-style date to European-style date')
print('Once files are found, the system will give option to either rename files or create a new file')
folderPath = input('Enter the file location (sample : C:/Test/Naresh/): ')
for foldername, subfolders, filenames in os.walk(folderPath):
    for filename in filenames:
        filesinDir[filename] = foldername + "\\"
 
if len(filesinDir) > 0:
    print('There are %s files in the directory'%(len(filesinDir))) 
totalFilesSearched =  len(filesinDir)   
print ('searching..........')     
time.sleep(1)
# Loop over the files in working directory
for keys in list(filesinDir):
    if datePattern.search(keys):
        continue
    else:
        filesinDir.pop(keys)
if len(filesinDir) > 0:
    print(f'Out of {totalFilesSearched} files in the directory, {(len(filesinDir))} files have filename in American name format and needs to change')  
    while True:
        backupFlag = int(input('Do you want to rename the existing file or create a new file with updated date format (1 for rename 2 for create): '))
        if backupFlag == 1 or 2:
            break
        else:
            print('Invalid character. Please enter 1 or 2')
# Form the European-style filename
if backupFlag == 1:
    renameFiles(filesinDir)
else:
    createFiles(filesinDir)


