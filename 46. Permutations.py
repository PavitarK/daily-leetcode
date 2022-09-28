"""
Leetcode Problem 46
Permutations
"""

def permute(nums): 
    # the number of elements in input == output 
    # the elements show up the same # of times in the input as output
    if len(nums) <= 1: 
        return [nums]
        
    permutations = [[]] 
    
    for num in nums:
        new_combos = []
        for perm in permutations:
            for i in range(len(perm)+1): 
                new_combos.append(perm[:i] + [num] + perm[i:])
        
        permutations = new_combos
    
    return permutations
    