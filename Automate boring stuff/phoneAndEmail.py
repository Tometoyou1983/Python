#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
# diferent attributes we can use for regex
#\d ==> Any numeric digit from 0 to 9.
#\D ==> Any character that is not a numeric digit from 0 to 9.
#\w ==> Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
#\W ==> Any character that is not a letter, numeric digit, or the underscore character.
#\s ==> Any space, tab, or newline character. (Think of this as matching “space” characters.)
#\S ==> Any character that is not a space, tab, or newline.
#{ ==> is used for grouping
#| ==> pipe character. User like a or condition
#? ==> Optional match.that is regex should 


import os, pyperclip, re
os.system('cls')

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+              # username
    @                              # symbol
    [a-zA-Z0-9.-]+                 # domain name
    (\.[a-zA-Z])?              # dot-somethin
    )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] !='':
        phoneNum += ' x' + groups[8]      
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    email =  groups[0]
    matches.append(email)
    

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails addresses found')