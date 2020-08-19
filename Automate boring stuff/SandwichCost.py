import os, pyinputplus as pyip, time
os.system("cls")

prices = {"wheat": 1.45,
          "white" : 1.15,
          "sourdough": 1.75,
          "chicken" : 0.90,
          "turkey" : 1.45, 
          "ham" : 1.35,
          "tofu" : 0.75,
          "cheddar": 0.25,
          "Swiss": 0.35,
          "mozzarella": 0.4,
          "mayo": 0.25,
          "mustard": 0.25,
          "lettuce": 0.5,
          "tomato": 0.5
          }
sandwichCost = 0
selectionitems = []
print("Welcome to Hungry Jacks")
time.sleep(1)
print("Select the bread type from the following:")
selectionitems.append(pyip.inputMenu(['wheat', 'white', 'sourdough']))
print("Select the protien from the following:")
selectionitems.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], blank=True))
cheese = pyip.inputYesNo(prompt="Do you want cheese: ")
if cheese == "yes":
    selectionitems.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']))
while True:
    addon = pyip.inputYesNo(prompt="Anything else to add on. Would you like to look at the options: ")
    if addon == "yes":
        selectionitems.append(pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato']))
    if addon == "no":
        break
numofSandwiches = pyip.inputNum(prompt="Enter number of sandwiches: ", min=1)
for i in range(len(selectionitems)):
        sandwichCost = sandwichCost + prices[selectionitems[i]]

print("Cost per Sandwich is: $%s" %sandwichCost)
print("Total cost of your order is: $%s" %(sandwichCost*numofSandwiches))
