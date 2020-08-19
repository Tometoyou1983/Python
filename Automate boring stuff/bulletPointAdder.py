#automatically adding stars to a list of lines
import os, pyperclip

os.system("cls")

text = pyperclip.paste()
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines) # join lines since pyperclip is expecting one big text
pyperclip.copy(text)
