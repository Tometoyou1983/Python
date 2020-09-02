#python 3
#This program creates a schedule to look at set of websites and downloads any new content uploaded.
#Any images that are availabe after last visit will get downloaded.
#System also asks user to provide a specific date that user wants to download images after for the first time.
#Scheduled to run once every day.
# the list of website we are looking for is
# 1. https://www.buttersafe.com/ can use archive tab to compare dates
# 2. https://www.savagechickens.com/ archive tab at the bottom (not developed yet)
# 3. http://www.lunarbaboon.com/ doesnt have archive. need to check for page level or some other option (not developed yet)
# 4. https://www.exocomics.com/ can use archive path here as well (not developed yet)
# only running search on sites that updated in 2020 for testing sake 
# this program also uses 4 different threads to search websites and write to respective folders seperately 
# with the date run as new folder. If the folder exists, it will just write to the folder.

import os, requests, bs4, time, re, sys, shelve
from datetime import datetime
os.system('cls')

urldct = {
        'buttersafe' : ['https://www.buttersafe.com/', 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/comics/Buttersafe/'] ,
#        'savagechickens' : ['https://www.savagechickens.com/', 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/comics/savagechickens/'] ,
#        'lunarbaboon' : ['http://www.lunarbaboon.com/', 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/comics/lunarbaboon/'] ,
#        'exocomics' : ['https://www.exocomics.com/', 'C:/Users/NagaVenkataSuryaNare/Documents/Naresh/comics/exocomics/']
}
# Create schedule


dateregex = '(?<=\d\w)(st|nd|rd|th)($<=\d\w)'
#check if the folders are existing or not for one time load
def checkDirectoryBeforeLoad (dirPath):
        try:
            os.listdir(dirPath)
            return False
        except:
            os.mkdir(dirPath)
            return True
def getCorrectdateLink(soup):
    prevLink = soup.select('a[rel="prev"]')[0]
    url = prevLink.get('href')
    return url
# download images
def downloadImages(url, soup, downloadPath):
    print(downloadPath)
    try:
        comicElem = soup.select('#comic img')
    except Exception as exc:
        print(f'something wrong with error code {str(exc)}')
    if comicElem == []:
        print('Could not find comic page')
    else:
        try: 
            comicurl = comicElem[0].get('src')
            #download the image
            print('Downloading image %s...' %(comicurl))
            res = requests.get(comicurl, headers={'User-Agent': 'Mozilla/5.0'})
            res.raise_for_status()
            prevLink = soup.select('a[rel="prev"]')[0]
            url = prevLink.get('href')
        except requests.exceptions.MissingSchema:
            #skip this comic
            prevLink = soup.select('a[rel="prev"]')[0]
            url = prevLink.get('href')
      
    
    imageFile = open(os.path.join(downloadPath, os.path.basename(comicurl)), 'wb')

    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    return url  
# load point for one time load
def getImagesfromWebsites(urldct, fromDate, toDate):
    url = urldct[0]
    downloadPath = urldct[1]
    while True:       
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        res.raise_for_status()
        soup =  bs4.BeautifulSoup(res.text,"lxml")
        
        try:
            comicDate = soup.find(True, {'class': 'comicdate'}).text.strip()
            comicDateFormat = re.sub(r"\b([0123]?[0-9])(st|th|nd|rd)\b",r"\1", comicDate)
            comicDateFormat = datetime.strftime(datetime.strptime(comicDateFormat, "%A, %B %d, %Y :: %I:%M %p"), "%m/%d/%Y")
            if (comicDateFormat <= toDate) and (comicDateFormat >= fromDate):
                url =  downloadImages(url, soup, downloadPath)
            elif comicDateFormat < fromDate:
                break
            else:    
                url = getCorrectdateLink(soup)
            
    # Find the URL of the comic image.
        except:
            print(f'Something went wrong. stopping the program for now')
            sys.exit()
    

def schedule():
    time.sleep(5)
# main function that does everything
def main():
    currdate = datetime.now()
    currDate = currdate.strftime("%m/%d/%Y")
#    currDate = '08/31/2020'

    print(f'current date is {currDate}')
    try:
        dateShelve = shelve.open('C:/Users/NagaVenkataSuryaNare/Documents/Naresh/comics/dateShelf.db', writeback=True)
        existing = dateShelve['prevDate']
        
    except:
        dateShelve['prevDate'] = currDate
        while True:
            searchDate = input('Enter date you want to search in MM/DD/YYYY format: ')
            try:
                validDate = datetime.strptime(searchDate, "%m/%d/%Y") 
                if searchDate > currDate:
                    print('Cant download anything from future.')
                break
            except:
                print('Invalid Date format. Please try again') 
      
    for keys in urldct:
        firsttimeload =  checkDirectoryBeforeLoad(urldct[keys][1])
        if firsttimeload:
            print(f'first time loading {urldct[keys][1]}')
            prevDate = searchDate
            getImagesfromWebsites(urldct[keys], prevDate, currDate)
            dateShelve['prevDate'] = currDate
        else:
            prevDate = dateShelve['prevDate']
            getImagesfromWebsites(urldct[keys], prevDate, currDate) 
            
    dateShelve['key'] = currDate
    dateShelve.sync()
    dateShelve.close()



# Look websites one after the 
# download content from website or post error that there is no new content
if __name__== "__main__":
    main()
