"""
Leetcode Problem 70
Climbing Stairs
"""    
import itertools
    
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    add = True
    twos = 1 
    total = 1
    
    while add: 
        set = []
        unique = []
        
        for _ in range(twos): 
            set.append(2)
        
        if sum(set) > n: 
            return (total)
        
        else: 
            while sum(set) < n: 
                set.append(1)
    
        result = itertools.permutations(set)
        
        for combo in list(result): 
            if combo not in unique: 
                unique.append(combo)
        
        total += len(unique)
        twos += 1
        print(len(unique))       
        
            

print(f"There are {climbStairs(n=5)} ways to climb to the top")