# Python 3
# This program takes user input to search for specific string in Flickr
# Once done, it will allow user to select if he wants to sort on relevant, date uploaded, date taken interesting
# Once sorted, it will ask user how many photos to download and to which location
# Once info is provided, the relevant pictures will be downloaded to the diretory user provided.

import os, sys, platform, time,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

os.system('clear')

print("Lets download some pictures from Flickr")
print('The default search string is photography')
searchStr = input("Enter the string you want to search: ")
if searchStr == '':
    searchStr = 'photography'

while True:
    preference = int(input("Enter selection 1 for Relevant, 2 for Date Uploaded, 3 for Date Taken, 4 for Interesting: "))
    if preference == 1:
        sortStr = 'relevance'
        break
    elif preference == 2:
        sortStr = 'date-posted-desc'
        break
    elif preference == 3:
        sortStr = 'date-taken-desc'
        break
    elif preference == 4:
        sortStr = 'interestingness-desc' 
        break
    else:   
        print('Invalid entry. Please enter valid selection')

noOfDownloads = int(input('Enter number of images you want to download: '))
locationDownload = input('Enter path to download images to: ')
#locationDownload = '/Users/naninenu/Downloads/Flickr/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options = options, executable_path="/Users/naninenu/Documents/Python/AutomateBoringStuff/chromedriver")

browser.get('https://www.flickr.com/search/?text=' + searchStr + '&sort=' + sortStr ) 
browser.maximize_window()
time.sleep(5)
imagesList = []
count = 0
pics = browser.find_elements_by_xpath('//div[@class="photo-list-photo-interaction"]/a[@class="overlay"]')
for i in range(noOfDownloads):
    imagesList.append(pics[i].get_attribute('href'))
    print('saving images to directory you provided')
time.sleep(1)
for i in range((len(imagesList))): 
    browser.get(imagesList[i])
    url = browser.find_element_by_xpath('//div[@class="view photo-well-media-scrappy-view requiredToShowOnServer"]/img[2]').get_attribute('src')
    res=requests.get(url)
    imageFile = open(os.path.join(locationDownload,os.path.basename(url)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    count += 1
    print ('image %s downloaded.' %count )
    time.sleep(1)
browser.close()
