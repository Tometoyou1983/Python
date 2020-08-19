import os, sys
os.system('cls')

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(stuff):
    print("Inventory: ")
    item_total = 0
    for keys, value in stuff.items():
        print(str(value) + " " + keys)
        item_total = item_total + value
    print("Total number of items: " + str(item_total))

def addToInventory(stuff, addedItems):
    for i in range(len(addedItems)):
        key = addedItems[i]
        if key in stuff:
            stuff[key] =  stuff[key] + 1 
        else:
            stuff.setdefault(addedItems[i], 1)    
    return stuff    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
invent = addToInventory(inv, dragonLoot)

displayInventory(invent)