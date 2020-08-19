# ! python3
# mcb.pyw - Saves and reloads the pieces of text to the clipboard
# usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw list - Loads all keywords to clipboard
#        py.ext mcb.pyw delete <keyword> - deletes keyword from clipboard
#        py.ext mcb.pyw delete  deletes the complete files
import shelve, pyperclip, sys, os

mcbshelf = shelve.open('mcb')

def deletemcb():
    for Keywords in list(mcbshelf.keys()):
        del mcbshelf[Keywords]
    mcbshelf.close()
    os.remove('mcb.dat')
    os.remove('mcb.dir')
    os.remove('mcb.bak')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcbshelf:
        del mcbshelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
        print(list(mcbshelf.keys()))
    if sys.argv[1].lower() == 'delete':
        deletemcb()
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()
