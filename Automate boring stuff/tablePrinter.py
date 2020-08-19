import os
os.system("cls")

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']] 

def printTable(grid):
    x = y = 0
    colWidth = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            word = grid[i][j]
            wordLength = len(word)
            if colWidth < wordLength:
                colWidth = wordLength

    for y in range(len(grid[x])): 
        for x in range(len(grid)): 
            newword = grid[x][y].ljust(colWidth)         
            print(newword, end=" ")
        print("\n")
        

printTable(tableData)