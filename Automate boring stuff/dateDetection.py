
# 01/10/2019
# 12/22/2019
# 31/01/2999
# 31/12/9999
# 31/12/0999
# 31/13/0999
# 33/13/0999
# 00/00/0000
# 23/12/2042
import os, pyperclip, re
os.system('cls')

DateRegex = re.compile(r'''((0[1-9]|[1-2][0-9]|3[0-1])?/([0][1-9]|1[0-2])?/[1-2][0-9][0-9][0-9])''')

text = str(pyperclip.paste())
matches = []

for groups in DateRegex.findall(text):
    validDate =  groups[0]
    matches.append(validDate)
    

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No Valid date fields found')