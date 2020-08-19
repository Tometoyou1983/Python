# python 3
# This program reads all the files in the directory location provided by user 
# and looks for keywords such as ADJECTIVE, NOUN, ADVERB, OR VERB
# If the program finds any of these in the directory, it will prompt the user to enter values for these. There are 3 different criteria:
#  1. Allow the user to update the value entered on  all files
#  2. Allow the user to update the values for each file seperately based on what is found
#  3. Allow the user to specify a file name and then allow him to update that specific file.
# once updated, results will be shown with what each file has been updated with. If there are no changes, we will print no changes on the terminal
#  

import os, time, re, path
os.system('cls')

def updateAllFiles(filesinDir):
    nounRegex = re.compile(r'''\bNOUN\b''', re.I)
    noun1Regex = re.compile(r'''\bNOUN1\b''', re.I)
    adJRegex = re.compile(r'''\bADJECTIVE\b''', re.I)
    advRegex = re.compile(r'''\bADVERB\b''', re.I)
    verbRegex = re.compile(r'''\bVERB\b''', re.I)
    updatedFiles =[]
    replacementWords = {}
    print("Searching all files for valid keywords to replace")
    for files in range(len(filesinDir)):
        filename = folderPath + filesinDir[files]
        data = open(filename, 'r').read()
        
        if re.findall(noun1Regex, data):
             replacementWords['NOUN1'] = ""
        if re.findall(nounRegex, data):
           replacementWords['NOUN'] = ""
        if re.findall(adJRegex, data):
             replacementWords['ADJECTIVE'] = ""
        if re.findall(advRegex, data):
            replacementWords['ADVERB'] = ""
        if re.findall(verbRegex, data):
            replacementWords['VERB'] = ""
    for keys in replacementWords:
        replacementWords[keys] = input(f'Enter a {keys} to replace: ')
    for files in range(len(filesinDir)):
        filename = folderPath + filesinDir[files]
        data = open(filename, 'r').read()
        written = False
        if (re.findall(nounRegex, data) or re.findall(noun1Regex, data) or re.findall(adJRegex, data) or       \
           re.findall(advRegex, data) or  re.findall(verbRegex, data)):
            written =  True
            for keys in replacementWords:
                data = data.replace(keys, replacementWords[keys])
        if written == True:
            with open(filename,'w') as file:
                file.write(data)      
            updatedFiles.append(filesinDir[files])
    return (updatedFiles)
def updateIndividualFiles(filesinDir):
    nounRegex = re.compile(r'''\bNOUN\b''', re.I)
    noun1Regex = re.compile(r'''\bNOUN1\b''', re.I)
    adJRegex = re.compile(r'''\bADJECTIVE\b''', re.I)
    advRegex = re.compile(r'''\bADVERB\b''', re.I)
    verbRegex = re.compile(r'''\bVERB\b''', re.I)
    for files in range(len(filesinDir)):
        replacementWords = {}
        keysWeHave = ""
        filename = folderPath + filesinDir[files]
        print('searching %s for keywords' %filesinDir[files])
        data = open(filename, 'r').read()   
        if re.findall(noun1Regex, data):
             replacementWords['NOUN1'] = ""
        if re.findall(nounRegex, data):
           replacementWords['NOUN'] = ""
        if re.findall(adJRegex, data):
             replacementWords['ADJECTIVE'] = ""
        if re.findall(advRegex, data):
            replacementWords['ADVERB'] = ""
        if re.findall(verbRegex, data):
            replacementWords['VERB'] = ""
        for keys in replacementWords:
            if keysWeHave == '':
                keysWeHave = keys
            else:    
                keysWeHave = keysWeHave + ', ' + keys
        if keysWeHave == '':
            print("We didnot find any keywords on this file. Not updating the file.")
        else:
            print('we found these keywords: %s' %keysWeHave)
            for keys in replacementWords:
                replacementWords[keys] = input(f'Enter a {keys} to replace: ')
            written = False
            if (re.findall(nounRegex, data) or re.findall(noun1Regex, data) or re.findall(adJRegex, data) or       \
            re.findall(advRegex, data) or  re.findall(verbRegex, data)):
                written =  True
                for keys in replacementWords:
                    data = data.replace(keys, replacementWords[keys])
            if written == True:
                with open(filename,'w') as file:
                    file.write(data)      
                print(filesinDir[files] + ' has been updated')

def updatespecificFiles(selectedFile):
    print("Searching in the %s for keywords" %selectedFile)
    nounRegex = re.compile(r'''\bNOUN\b''', re.I)
    noun1Regex = re.compile(r'''\bNOUN1\b''', re.I)
    adJRegex = re.compile(r'''\bADJECTIVE\b''', re.I)
    advRegex = re.compile(r'''\bADVERB\b''', re.I)
    verbRegex = re.compile(r'''\bVERB\b''', re.I)
    for files in range(len(filesinDir)):
        replacementWords = {}
        keysWeHave = ""
        if filesinDir[files] == selectedFile:
            filename = folderPath + filesinDir[files]
            print('searching %s for keywords' %filesinDir[files])
            data = open(filename, 'r').read()   
            if re.findall(noun1Regex, data):
                replacementWords['NOUN1'] = ""
            if re.findall(nounRegex, data):
                replacementWords['NOUN'] = ""
            if re.findall(adJRegex, data):
                replacementWords['ADJECTIVE'] = ""
            if re.findall(advRegex, data):
                replacementWords['ADVERB'] = ""
            if re.findall(verbRegex, data):
                replacementWords['VERB'] = ""
            for keys in replacementWords:
                if keysWeHave == '':
                    keysWeHave = keys
                else:    
                    keysWeHave = keysWeHave + ', ' + keys
            if keysWeHave == '':
                print("We didnot find any keywords on this file. Not updating the file.")
                break
            print('we found these keywords: %s' %keysWeHave)
            for keys in replacementWords:
                replacementWords[keys] = input(f'Enter a {keys} to replace: ')
            written = False
            if (re.findall(nounRegex, data) or re.findall(noun1Regex, data) or re.findall(adJRegex, data) or       \
            re.findall(advRegex, data) or  re.findall(verbRegex, data)):
                written =  True
                for keys in replacementWords:
                    data = data.replace(keys, replacementWords[keys])
            if written == True:
                with open(filename,'w') as file:
                    file.write(data)      
                print(filesinDir[files] + ' has been updated')


print('This program searches for specific keywords in all the text files we have in a specific directory and prompts user to enter values to update it')
print("The keywords we are looking for are: 'ADJECTIVE', 'NOUN1', 'NOUN2', 'ADVERB', 'VERB'" )
time.sleep(1)
folderPath = input('Enter the file location (sample : C:/Test/Naresh/): ')
filesinDir = [x for x in os.listdir(folderPath) if x.endswith(".txt")]
if len(filesinDir) > 0:
    print('There are %s .txt files in the directory'%(len(filesinDir)))    
for files in range(len(filesinDir)):
    print(filesinDir[files])
time.sleep(1)
print("You have 3 options to choose from")
print("Enter 1 for search and update all files")
print("Enter 2 for looping thru each file and entering the required values")
print("Enter 3 for selecting the file name on which you want to search and update data")
while True:
    activityType =  int(input("Enter your selection:  "))
    if activityType == 1:
        updatedFilesList = updateAllFiles(filesinDir)
        if len(updatedFilesList) > 0:
            print ("Updated %s files" %len(updatedFilesList))
            print ("Files updated are:")
            for i in range(len(updatedFilesList)):
                print(updatedFilesList[i])
        break
    elif activityType == 2:
        updateIndividualFiles(filesinDir)
        break
    elif activityType == 3:
        selectedFile =  input("Enter the file name (sample: filename.txt): ")
        updatespecificFiles(selectedFile) 
        break
    else:
        print("Not a valid selection. select 1 or 2 or 3")   



