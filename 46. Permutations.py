"""
Leetcode Problem 46
Permutations
"""

def permute(nums): 
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
    