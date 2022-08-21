"""
Leetcode Problem 36
Valid Sudoku
"""

def isValidSudoku(board): 
    return checkRows(board=board) and checkCol(board) and checkSquare(board)

def checkRows(board):
    for row in range(9):
        col = 0
        found = []
        while col < 9:  
            if board[row][col] != '.':
                if board[row][col] in found: 
                    return False
                else: 
                    found.append(board[row][col])
            col += 1 
    
    return True

def checkCol(board): 
    for col in range(9): 
        row = 0 
        found = []
        while row < 9: 
            if board[row][col] != '.':
                if board[row][col] in found:
                    return False
                else: 
                    found.append(board[row][col])
            row += 1 
     
    return True

def checkSquare(board):
    row_group = 0
    col_group = 0
    found = []
    
    #check each square 
    while row_group < 9:
        for i in range(3):
            row = i + row_group 
            for j in range(3): 
                col = j + col_group
                check = board[row][col]
                if check !='.':
                    if check in found: 
                        return False
                    else: 
                        found.append(check)
        # once done checking 3 rows go to next column group
        # if have completed all column groups go to next 
        # row group and reset found and column count since 
        # starting a new square. 
        if col_group == 6: 
            row_group +=3
            col_group = 0
        else: 
            col_group +=3

        found = []
       
    return True


board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


print(isValidSudoku(board))