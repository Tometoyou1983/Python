# webscrapping basics program

import webbrowser, os, sys, pyperclip

os.system('cls')

if len(sys.argv) > 1:
    #Get address from command line
    address = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    address =  pyperclip.paste()
    if address == '':
        address = input('Enter a address to mapIT')

webbrowser.open('https://www.google.com/maps/place/' + address)