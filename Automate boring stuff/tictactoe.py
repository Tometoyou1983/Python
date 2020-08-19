import os, datetime, sys
os.system('cls')

# defining the table
theBoard = {'top-L':' ', 'top-M':' ','top-R':' ',
           'mid-L':' ', 'mid-M':' ','mid-R':' ',
           'low-L':' ', 'low-M':' ','low-R':' ',}
def printBoard(board):
    print ('________________')
    print ('| ' + board['top-L'] + '  |  ' + board['top-M'] + '  |  '+ board['top-R'] + ' |')
    print ('-----+-----+----')
    print ('| ' + board['mid-L'] + '  |  ' + board['mid-M'] + '  |  '+ board['mid-R'] + ' |')
    print ('-----+-----+----')
    print ('| ' + board['low-L'] + '  |  ' + board['low-M'] + '  |  '+ board['low-R'] + ' |')
    print ('________________')
# load the table
def loadtable(nxtMove, playerMove):
    theBoard[nxtMove] = playerMove
# determine player turn
def determinevalidmoves ():
    Validmoves = ""
    for key, value in theBoard.items():
        if value == ' ':
            if Validmoves == "":
                Validmoves = key
            else:
                Validmoves = Validmoves + ", " + key
        
    nxtMove = input("Valid options are (" + Validmoves + "): ")
    while True:
        if nxtMove in theBoard.keys():
            if theBoard[nxtMove] != ' ':
                print ("That column is already selected")
                nxtMove = input("Valid options are (" + Validmoves + "): ")
            else:
                break
        else:
            print ("That's an invalid selection")
            nxtMove = input("Valid options are (" + Validmoves + "): ")
    return nxtMove 

def detturn(player1turn,player2turn):
    if player1turn == True:
        playerMove = 'X'
        print(player1 + "'s turn. Please pick a move by mentioning the name")
        nxtMove = determinevalidmoves()
        loadtable(nxtMove, playerMove)
        printBoard(theBoard)
        player1turn =  False
        player2turn = True
        return player1turn, player2turn
    if player2turn == True:
        playerMove = 'O'
        print(player2 + "'s turn. Please pick a move by mentioning the name")
        nxtMove = determinevalidmoves()
        loadtable(nxtMove,playerMove)
        printBoard(theBoard)
        player2turn =  False
        player1turn = True  
        return player1turn, player2turn   
def detWinner(board):
    winner = ""
    if (board['top-L'] == 'X' and board['top-M'] == 'X' and board['top-R'] == 'X') or \
       (board['mid-L'] == 'X' and board['mid-M'] == 'X' and board['mid-R'] == 'X') or \
       (board['low-L'] == 'X' and board['low-M'] == 'X' and board['low-R'] == 'X') or \
       (board['top-L'] == 'X' and board['mid-M'] == 'X' and board['low-R'] == 'X') or \
       (board['top-R'] == 'X' and board['mid-M'] == 'X' and board['low-L'] == 'X') or \
       (board['top-L'] == 'X' and board['mid-L'] == 'X' and board['low-L'] == 'X') or \
       (board['top-M'] == 'X' and board['mid-M'] == 'X' and board['low-M'] == 'X') or \
       (board['top-R'] == 'X' and board['mid-R'] == 'X' and board['low-R'] == 'X'):
       winner = 'X'
    elif (board['top-L'] == 'O' and board['top-M'] == 'O' and board['top-R'] == 'O') or \
       (board['mid-L'] == 'O' and board['mid-M'] == 'O' and board['mid-R'] == 'O') or \
       (board['low-L'] == 'O' and board['low-M'] == 'O' and board['low-R'] == 'O') or \
       (board['top-L'] == 'O' and board['mid-M'] == 'O' and board['low-R'] == 'O') or \
       (board['top-R'] == 'O' and board['mid-M'] == 'O' and board['low-L'] == 'O') or \
       (board['top-L'] == 'O' and board['mid-L'] == 'O' and board['low-L'] == 'O') or \
       (board['top-M'] == 'O' and board['mid-M'] == 'O' and board['low-M'] == 'O') or \
       (board['top-R'] == 'O' and board['mid-R'] == 'O' and board['low-R'] == 'O'):
       winner = 'O'
    return winner
#intro message
nxtgame = "Yes"
while nxtgame == "Yes":
    print ("Lets play a 2 player Tic-Tac-Toe Game..")
    theBoard = {'top-L':' ', 'top-M':' ','top-R':' ',
           'mid-L':' ', 'mid-M':' ','mid-R':' ',
           'low-L':' ', 'low-M':' ','low-R':' ',}
    printBoard(theBoard)
    player1 =  input("Enter player 1 name: ")
    player2 =  input("Enter player 2 name: ")
    player1turn = True
    player2turn =  False
    whoisWinner = ""
    print (player1 + " starts")
    for i in range(len(theBoard)):
        whoisWinner = detWinner(theBoard)
        if whoisWinner == 'X':
            print(player1 + " wins. Better luck next time " + player2)
            break
        if whoisWinner == 'O':
            print(player2 + " wins. Better luck next time " + player1)
            break
        player1turn, player2turn = detturn(player1turn,player2turn)
    if whoisWinner == "": 
        print("Game is a Tie. Next time better luck")
    nxtgame = input("Would you like to play again? (Yes/No): ")
    if nxtgame == "No":
        sys.exit()




