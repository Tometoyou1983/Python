# ! python3
# Selenium controlled web browser.
# Author suggested using firefox. trying to use chrome.
#to use chrome, we need chrome driver  copied on the machine and the path provided.

import os, sys, bs4, requests
from selenium import webdriver
os.system('cls')
driver_path = "C:/Users/NagaVenkataSuryaNare/Documents/GitHub/Python/Python web programs/"
#driver = webdriver.Chrome(driver_path)

browser =  webdriver.Firefox(driver_path)
browser.get('http://inventwithpython.com')

try:
    elem = browser.find_element_by_class_name('bookcover')
    print('Found <%s> element with that class name!' %(elem.tag_name))
except:
    print('Was not able to find an element with that name')
