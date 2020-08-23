# ! python3
#googleFeelingLucky.py - Opens several Google search results

import os, requests, sys, webbrowser, bs4, datetime, time

os.system('cls')

if len(sys.argv) > 1:
    print('Googling.....')
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]),)
else:
    searchSrt = input("Enter the string you want to search: ")
    print('Googling.....')
    res = requests.get('http://google.com/search?q=' + searchSrt )
try:
    res.raise_for_status()
    # retrieve top search result links
    soup =  bs4.BeautifulSoup(res.text, "html.parser")
    # open a browser tab for each result
    linkElems = soup.select('.kCrYT > a')
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
    #    print('http://google.com' + linkElems[i].get('href'))
        webbrowser.open('http://google.com' + linkElems[i].get('href'))

except Exception as exc:
    print('Errored with %s' %(exc))