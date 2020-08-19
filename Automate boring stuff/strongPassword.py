import os, re
os.system('cls')

strongPass = re.compile(r'''([a-zA-z0-9#!$]{8,})''')
noCapital = re.compile(r'''([a-zA-z0-9#!$]{8,})''')

while True:
    text = input("Enter a password. Please have min of 8 character/number with atleast 1 special character: ")
    pattern = "^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&_=]).*$"
    result = re.findall(pattern, text)
    if result:
        print("Valid password")
        break
    else:
        print("You didnot meet the password entry criteria. Please try again")
        