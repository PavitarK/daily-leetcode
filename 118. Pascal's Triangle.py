"""
Leetcode Problem 118
Pascal's Triangle
"""


# First solution
def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if numRows == 1: 
        return [[1]]
    
    pascal = [[1]]
    
    for row in range(2,numRows+1): 
        build = [1] * row
        to_fill = row - 2
        if to_fill: 
            for i in range(to_fill): 
                build[i+1] = pascal[row-2][i] + pascal[row-2][i+1]
        pascal.append(build)        
            
    return pascal

# Faster and uses less memory solution!
def generate_fast(numRows):
    pascal = []
    prev_row = [1]
    
    for i in range(1,numRows+1): 
        curr_row = [1] * i
        for val in range(i): 
            if val == 0: 
                curr_row[val] = 1
            elif val == i-1: 
                curr_row[val] = 1
            else: 
                curr_row[val] = prev_row[val-1] + prev_row[val]
        pascal.append(curr_row)
        prev_row = curr_row
        
    return pascal    
print(f"Result is: {generate_fast(5)}")