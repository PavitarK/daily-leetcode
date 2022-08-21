"""
Leetcode Problem 70
Climbing Stairs
"""    
import itertools
    
def climbStairs(n):
    """
    :type n: int
    :rtype: int
    
    Naive approach. This works but takes too much memory and is too slow. 
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
        

def climbStairsRecursive(n): 
    """
    In this approach we are using the knowledge that getting to stair x
    in steps of 1 and 2 is equal to how ways we can get to x-1 and x-2.
    
    This works but is too slow. 
    """
    
    if n == 1 or n == 0: 
        return 1
    
    else: 
        return climbStairsRecursive(n-1) + climbStairsRecursive(n-2)

def climbStairsDynamicFast(n): 
    """
    Using the same recursive logic however can speed things up by removing 
    redundant calculations. For example if we have calculated climbStairs(2)
    we don't need to do it again and again. 
    
    Instead keep an array to look up values build bottom up.
    [1,1,2,3,5,8....]
    """
    # ways 0 and 1 are always 1, build pattern from there
    ways = [1,1]
    
    for i in range(2,n+1): 
        ways.append(ways[i-1] + ways[i-2])
        
    return ways[n]    
    

print(f"There are {climbStairsDynamicFast(n=40)} ways to climb to the top")