"""
Leetcode Problem 326
Power of Three
"""

def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0: 
        return False
            
    if n == 1: 
        return True
    
    if n % 3 != 0: 
        return False
    
    return self.isPowerOfThree(n=n/3)

n = 65536
print(f"Is {n} a power of three? {isPowerOfThree(n)}")