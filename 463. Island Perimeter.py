"""
Leetcode Problem 463
Island Perimeter
"""   

def islandPerimeter(grid): 
    
    perimeter = 0 
    maxRow = len(grid)
    maxCol = len(grid[0])
    # parse grid
    for row in range(maxRow): 
        for col in range(maxCol): 
            # increase perimeter count at every 1
            # do not go beyond grid limits
            if grid[row][col] == 1: 
                add = 4
                if row != 0: 
                    if grid[row-1][col] == 1: 
                        add -= 1
                if row != maxRow-1: 
                    if grid[row+1][col] == 1: 
                        add -= 1 
                if col != maxCol-1: 
                    if grid[row][col+1] == 1: 
                        add -=1
                if col != 0: 
                    if grid[row][col-1] == 1: 
                        add -=1
                perimeter += add
    
    return perimeter

grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
print(f"permimeter is {islandPerimeter(grid)}")