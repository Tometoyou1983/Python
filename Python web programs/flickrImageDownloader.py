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
#locationDownload = 'input('Enter path to download images to: ')
locationDownload = '/Users/naninenu/Downloads/Flickr/'

options = webdriver.ChromeOptions()
#options.add_argument('--headless')

browser = webdriver.Chrome(chrome_options = options, executable_path="/Users/naninenu/Documents/Python/AutomateBoringStuff/chromedriver")

browser.get('https://www.flickr.com/search/?text=' + searchStr + '&sort=' + sortStr ) 
browser.maximize_window()
time.sleep(5)
#relevantInfo = browser.find_element_by_xpath('//div[@class="dropdown-link sort-menu"]')
#relevantInfo.click()

#if preference == 1:
# print(browser.find_element_by_xpath("//div[starts-with(@id, 'yui_3_16_0_1') and @role='menuitem']").text)
pics = browser.find_element_by_xpath('//div[@class="view photo-list-photo-view requiredToShowOnServer awake"]')
pics.click()
count = 0
print('saving images to directory you provided')
time.sleep(3)
for i in range(noOfDownloads): 
    try:
        browser.find_element_by_xpath('//div[@class="photo-page-i-m-container"]')
        print('Ad encountered. waiting for 5 min')
        time.sleep(6)
        browser.find_element_by_xpath('//a[@class="navigate-target navigate-next"]/span[@class="hide-text"]').click()
        i = i - 1
    except:
        url = browser.find_element_by_xpath('//div[@class="view photo-well-media-scrappy-view"]/img[2]').get_attribute('src')
        res=requests.get(url)
        imageFile = open(os.path.join(locationDownload,os.path.basename(url)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        count += 1
        print ('image %s downloaded.' %count )
        time.sleep(2)
        browser.find_element_by_xpath('//a[@class="navigate-target navigate-next"]/span[@class="hide-text"]').click()
        time.sleep(5)

time.sleep(5)
browser.close()
