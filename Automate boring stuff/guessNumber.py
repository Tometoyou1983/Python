def avgNum (firstNum,lastNum) :
    secretNumber = int((firstNum + lastNum)/2)
    return secretNumber

print("Hello! welcome to guess the number game")
print("Guess a positive secret number integer between 1 and 100")
print("If i dont guess your number in 7 tries you win")
secretNumberFlag = "No"
numberTries = 0
secretNumber = 50
firstNum = 0
lastNum = 100
wonFlag = False
correctNumberFlag = "No"

for i in range(7):
    numberTries = numberTries + 1
    print("Try number: " + str(numberTries))
    print("Is your number  " + str(secretNumber) + " ? (Yes/No) ")
    correctNumberFlag = input()
    if correctNumberFlag == "Yes":
        print("Number you guessed is: " + str(secretNumber))
        print("It took " + str(numberTries) + " tries to guess your number")
        wonFlag = True
        break
    else: 
        print ("Is your number > " + str(secretNumber) + " ? (Yes/No")
        secretNumberFlag = input()
        if secretNumberFlag == "Yes":
           firstNum = secretNumber
        else:
            lastNum =  secretNumber
        secretNumber = avgNum(firstNum,lastNum)
        
if wonFlag:
    print("I won")
else:
    print("Bummer!, you won")    

    
        







    
