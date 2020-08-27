# Python 3
# This program verifies all the links given in the url page, checks for errors and if so report the link 
# as broken.
import os, sys, platform, time,requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.system('clear')

while True:
    inputLink = input('Enter the url you want us to test: ')
    if inputLink > "":
        break
    else:
        print('Invalid entry')

options = webdriver.ChromeOptions()
options.add_argument('--headless') # enable headless mode

browser = webdriver.Chrome(chrome_options = options, executable_path="/Users/naninenu/Documents/Python/AutomateBoringStuff/chromedriver")

browser.get(inputLink)
browser.maximize_window()
time.sleep(1)
invalidCount = 0
links = browser.find_elements_by_xpath('//a')

for i in range(len(links)):
    try:
        link = links[i].get_attribute('href') 
        res = requests.get(link)
        try:
            res.raise_for_status()
        except requests.exceptions.HTTPError:
            print (f'link {link} is invalid. Error: {res.status_code}')
            invalidCount += 1 
    except requests.exceptions.MissingSchema:
        print(f'{link} is not a valid url')
        continue
print(f'there are {invalidCount} not found links in the url you provided')
browser.close()

