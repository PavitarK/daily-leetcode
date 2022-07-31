"""
Leetcode Problem 6
Zigzag Conversion
"""

import numpy as np

"""
First brute force solution
Uses 2d array to build and store zig zag pattern
"""

def convert(s, numRows) -> str: 
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # check if 1
    if numRows == 1: 
        return s
    
    ### build 2d array ###
    numLetters = len(s)
    numDiagonal = numRows-2

    numCols = len(s)
    scramble = np.empty(shape=(numRows,numCols), dtype=str)
    
    ### fill array ###
    fill_array(s, numLetters, numRows, numDiagonal, scramble)
    final_string = ''
    print(scramble)

    ### read array ###
    for row in range(numRows): 
        for col in range(numCols): 
            if scramble[row][col] != '': 
                final_string += scramble[row][col]
                
    return final_string
    
def fill_array(s, numLetters, numRows, numDiagonal, scramble): 
    s = list(s)
    letter = 0  
    next_start = 0  
    
    while letter <= numLetters - 1: 
        column = next_start
        for i in range(numRows): 
            scramble[i][column] = s[letter]
            letter += 1
            if letter > numLetters-1:
                return scramble
        
        column += 1
        row = numRows - 2
        for i in range(numDiagonal):
            scramble[row][column] = s[letter]
            row -=1
            column +=1
            letter += 1
            if letter > numLetters-1:
                return scramble
            
        next_start = column

"""
Explanation: This method leverages the idea that the zig zag is 
only a pictorial device, doing a diagonal line is the same as 
just inserting letters in a row upwards. 

So instead of creating a whole zigzag we can simply rotate which 
row we insert the next letter into
"""

def fast_solution_convert(s, numRows): 
    if numRows == 1: 
        return s
    
    # create a list of lists of length numRows
    my_array = [''] * numRows 
    
    dir = 1
    row = 0 
    for letter in s: 
        my_array[row] += letter
        
        if row == numRows -1: 
            dir = -1
            
        if row == 0: 
            dir = 1
            
        row += dir
    
    return ''.join(my_array)

result = convert(s='PAYPALISHIRING', numRows=4)
result_2 = fast_solution_convert(s='PAYPALISHIRING', numRows=4)
print(result)
print(result_2)