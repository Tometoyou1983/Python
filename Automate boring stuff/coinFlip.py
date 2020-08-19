import os, random
os.system('cls')

headsTails = []
inaRowCountT = 0
inaRowCountH = 0
headsCount = 0
tailsCount = 0
flipCount = int(input("How many times do you want the system to flip? "))
streakCount = int(input("How many consequtive times for a steak: "))
if streakCount == 0:
    print("You entered 0. System is considering a default of 6")
    streakCount = 6
for i in range(flipCount):
    if random.randint(0,1) == 0:
        headsTails.append('H')
        headsCount += 1
    else:
        headsTails.append('T')
        tailsCount += 1
for i in range(len(headsTails) - streakCount):
    count = 1
    rowFlag = True
    j = i
    while True:
        if count == streakCount:
            break
        elif headsTails[j] == headsTails [j+1]:
            count += 1
        else:
            rowFlag = False
            break
        j += 1
    if rowFlag == True and headsTails[i] == 'T' and count > 0:
        inaRowCountT += 1
    elif rowFlag == True and headsTails[i] == 'H' and count > 0:
        inaRowCountH += 1

print("Number of times computer flipped heads is " + str(headsCount))
print("Number of times computer flipped tails is " + str(tailsCount))
print ("Number of times six tails: " + str(inaRowCountT))
print ("Number of times six heads: " + str(inaRowCountH))
print('Chance of streak: %s%%' % ((inaRowCountT+inaRowCountH) / 100))
        

