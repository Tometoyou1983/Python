import os, datetime
os.system('cls')

birthdays = {}

def validatedatetime (birthday):
    try:
        if datetime.datetime.strptime(birthday, "%m/%d/%Y"):
            return True
    except ValueError:
        return False
while True:
    name = input("Enter a name (press enter to quit): ")
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name )
    else:
        print("I dont have the birthday information for this person")
        bday = input("Enter a birthday in mm/dd/yyyy format: ")
        while True:
            sample = validatedatetime(bday)
            if sample == True:
              birthdays[name]   = bday
              print("Birthday Database updated")
              break
            else:
                print("Invalid date format")
                bday = input("Enter a birthday in mm/dd/yyyy format: ")

          