import os, requests

os.system('cls')

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
    playFile =  open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(10000):
        print(chunk)
        playFile.write(chunk)
    playFile.close()
except Exception as exc:
    print('There was a problem: %s' %(exc))

