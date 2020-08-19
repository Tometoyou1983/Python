import random, sys
print ("Lets play Rock, Scissors, Paper")
wins = 0
losses = 0
ties = 0
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        playerMove = input("Enter a move: (r)ock, (s)cissors, (p)aper, (q)uit: ")
        if playerMove == "q":
            sys.exit()
        elif playerMove == "r":
            print ("Your Pick: rocks")
            break
        elif playerMove == "s":
            print ("Your Pick: scissors")
            break
        elif playerMove == "p":
            print ("Your Pick: paper")
            break
        else:
            print("Am not that dumb. Let's try again")
            playerMove = input("Enter a move: (r)ock, (s)cissors, (p)aper, (q)uit: ") 
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = "r"
        print ("Computer Pick: rock")
    elif randomNumber == 2:
        computerMove = "s"
        print ("Computer Pick: scissors")
    elif randomNumber == 3:
        computerMove = "p"
        print ("Computer Pick: paper")
    if playerMove == computerMove:
        print("Its a Tie")
        ties = ties + 1
    elif playerMove == "r" and computerMove == "s":
        print("Rock beats scissors! You Win")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Paper beats rock! You Win')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Scissors beat paper! You Win')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Paper beats rock! You Lose')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Scissors beat paper! You Lose')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Rock beats scissors! You Lose')
        losses = losses + 1 


    

