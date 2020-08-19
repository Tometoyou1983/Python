'''
import os, sys
os.system("clear")
print("Lets introduce you to collatz sequence or problem")
print("its an algorithm that starts with an integer and with multiple sequences reaches at 1")

numTries = 0
accumlatedNum = ""
newNumber = 0
def collatz(number):
    if number % 2 == 0:
        newNumber = number // 2
    else:
        newNumber = 3 * number + 1
    return newNumber

try:
    while True:
        myInteger = int(input("Enter a integer: "))
        while (newNumber != 1):
            newNumber = collatz(myInteger)
            numTries = numTries + 1
            if accumlatedNum == "":
                accumlatedNum = accumlatedNum + str(newNumber)
            else:    
                accumlatedNum = accumlatedNum + ", " + str(newNumber)
            myInteger = newNumber
        print("It took " + str(numTries) + " tries to come to 1") 
        print("the sequence is: " + accumlatedNum)
        playAgain = input("Would you like to play again? (Yes/No) ")
        if playAgain == "Yes":
            continue
        else:
            sys.exit()

except ValueError:
    print("You did not enter an integer")
    myInteger = input("Enter a valid integer: ")

'''

import os, sys
os.system("clear")
print("Lets introduce you to collatz sequence or problem")
print("its an algorithm that starts with an integer and with multiple sequences reaches at 1")

def collatz(number):
    count = 0
    print(str(number))
    if number == 1:
        return count
    elif (number % 2 == 0):  
        count = (collatz(int(number /2)) + 1)       
    elif (number % 2 != 0):
        count = (collatz(int(3 * number + 1)) + 1)
        
    return count

try:
    while True:
        myInteger = int(input("Enter a integer: "))
        numTries = collatz(myInteger)
        print("It took " + str(numTries) + " tries to come to 1") 
        playAgain = input("Would you like to play again? (Yes/No) ")
        
        if playAgain == "Yes":
            continue
        else:
            sys.exit()

except ValueError:
    print("You did not enter an integer")
    myInteger = input("Enter a valid integer: ")

