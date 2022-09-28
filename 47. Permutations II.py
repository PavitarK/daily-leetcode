"""
Leetcode Problem 47
Permutations II
"""

# same approach as permutation 1, just checking for
# duplicates not before adding to the list
def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) <= 1: 
        return [nums]
    
    perms = [[]]
    
    # for every number
    for num in nums: 
        new_perms = []
        # for every permutation in the list
        for perm in perms:
            # for every spot in the length of each permutation 
            for i in range(len(perm)+1): 
                
                # insert the number into each empty spot in the permutation
                new = perm[:i] + [num] + perm[i:]
                
                # check if it's unique 
                if new not in new_perms: 
                    new_perms.append(new)
        
        perms = new_perms
            
    return perms

print(permuteUnique(nums=[1,2,3,4,4]))