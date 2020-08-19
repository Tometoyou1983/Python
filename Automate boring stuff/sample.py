# implementing loop function with sample program to enter name, age and provide number of names entered.
againFlag = "Yes"
numberofEntries = 0
def nameAndAge ():  
    myName = input("Hello! Who am i speaking with: ")
    print("It's good to see you " + myName)
    print("The length of your name is ", len(myName))
    myAge = int(input("What is your age " + myName + ": "))
    print("You will be " + str(int(myAge + 1)) + " in an year")
    

while againFlag ==  "Yes":
    numberofEntries = numberofEntries + 1
    nameAndAge()
    againFlag = input("Do you want to enter a new name? (Yes/No): ")   

print("You entered " + str(numberofEntries) + " names")




