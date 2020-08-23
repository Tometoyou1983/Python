# python 3
# downloadxkcd.py - downloads every single xkcd comic

import os, time, webbrowser, requests, os, bs4
os.system('cls')

url = 'http://xkcd.com'
os.mkdir('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/xkcd')

while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s....' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup =  bs4.BeautifulSoup(res.text)
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic page')
    else:
        try: 
            comicurl = 'http:' + comicElem[0].get('src')
            #download the image
            print('Downloading image %s...' %(comicurl))
            res = requests.get(comicurl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')
            continue

    # Save the image to ./xkcd. 
    imageFile = open(os.path.join('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/xkcd', os.path.basename(comicurl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

# get prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')


print('Done')