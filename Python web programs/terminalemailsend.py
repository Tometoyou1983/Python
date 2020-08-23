# Python 3
# this program triggers a selenium script to send out an email thru terminal
#this can be alterted to enter info thru command line as well as copy/paste data using pyperclip
#this asks for email id of recipient, subject and body
# this program also needs to be updated with ur user id and pass for logging into gmail.

import os, time, re,sys, platform
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.system('cls')
emailRegex = r'''[\w-]+@([\w-]+\.)+[\w-]+'''
os_base = platform.system()

while True:
    toemail = input('Enter a valid email id: ')
    result = re.finditer(emailRegex, toemail)
    if result:
        break
    else:
        print('invalid email')
subject = input('Enter subject for email: ' )
emailBody = input ('Enter Body of the email: ')
print(' Running the script.......') 

browser = webdriver.Chrome(executable_path="/Users/naninenu/Documents/Python/AutomateBoringStuff/chromedriver")

browser.get('https://gmail.com')

ac = browser.find_element_by_id('identifierId')
ac.clear()
#enter your id
ac.send_keys('Your email ID' + Keys.ENTER)
time.sleep(1)
ps = browser.find_element_by_name('password')
ps.clear()
#enter ur password
ps.send_keys('your email password' + Keys.ENTER)
time.sleep(5)
#find the compose button and click it
cs = browser.find_element_by_xpath("//div[@gh='cm']")
cs.click()
time.sleep(2)
#pop the browser open
pop=browser.find_element_by_xpath('//img[@alt="Pop-out"]')
pop.click()
time.sleep(2)
#identify where to recipient
to=browser.find_element_by_xpath('//textarea[@name="to"]')
to.send_keys(toemail + Keys.TAB + Keys.TAB)
time.sleep(2)
# Add subject line
sub = browser.find_element_by_xpath('//input[@name="subjectbox"]')
sub.send_keys(subject + Keys.TAB)
time.sleep(2)

# Add text message
body = browser.find_element_by_id(':9l')
body.send_keys(emailBody)
time.sleep(2)
body.send_keys(Keys.TAB)

if os_base == 'Darwin':
    body.send_keys(Keys.COMMAND + Keys.ENTER)
elif os_base == 'Windows':
    body.send_keys(Keys.LEFT_CONTROL+Keys.ENTER)


print("Email Sent")

