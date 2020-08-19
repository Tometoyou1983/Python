import os, sys
os.system("clear")

spam = []
while True:
    name = input("Enter a string: ")
    spam.append(name)
    moreDataFlag = input("Would you like to enter more? (Yes/No)")
    if moreDataFlag != "Yes":
        break
accumString = ""
for i in range(len(spam)-1):
    accumString = accumString +  spam[i] + " ,"
accumString = accumString + " and " + spam[-1]
print("The list you entered contains: " + accumString)

