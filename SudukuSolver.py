#define the board 0 fot empty spaces
board = [
    [ 3, 1, 6, 5, 7, 8, 0, 9, 2 ],
    [ 5, 2, 9, 0, 3, 4, 0, 6, 8 ],
    [ 4, 0, 7, 6, 2, 0, 5, 3, 1 ],
    [ 2, 6, 3, 0, 0, 0, 9, 8, 7 ],
    [ 9, 7, 0, 8, 0, 0, 1, 0, 0 ],
    [ 8, 5, 0, 7, 9, 2, 0, 0, 3 ],
    [ 1, 3, 8, 0, 4, 7, 0, 0, 6 ],
    [ 6, 0, 2, 3, 0, 1, 8, 7, 4 ],
    [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ]
]

#solve board function using recursion
def solveSuduku(brd):
    empty = getEmpty(brd)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if isValid(brd, i, (row, col)):
            brd[row][col] = i

            if solveSuduku(brd):
                return True

            brd[row][col] = 0

    return False


#print suduku board
def printBoard(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
            print("ـــــــــــــــــــــــ")

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(brd[i][j])

            else:
                print(str(brd[i][j]) + " ", end = "")


#find empty spaces in the board
def getEmpty(brd):
    for i in range(len(brd)):
        for j in range(len(brd[0])):
            if brd[i][j] == 0:
                return (i, j) #return row and column
    return None


#check if valid
def isValid(brd, num, position):
     
    #check row
    for i in range(len(brd[0])):
        if brd[position[0]][i] == num and position[1] != i:
            return False
    #check column   
    for i in range(len(brd)):
        if brd[i][position[1]] == num and position[0] != i:
            return False

    #check squares
    horizontalSquare = position[1] // 3
    verticalSquare = position [0] // 3

    for i in range(verticalSquare*3, verticalSquare*3 + 3):
        for j in range(horizontalSquare*3, horizontalSquare*3 + 3):
            if brd[i][j] == num and (i, j) != position:
                return False
    
    return True



#print the solution
print("Board Before Solving: ")
printBoard(board)
solveSuduku(board)
print("Board After Solving: ")
printBoard(board)