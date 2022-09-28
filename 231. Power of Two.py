"""
Leetcode Problem 231
Power of Two
"""

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    
    if n == 1: 
        return True
    
    if n == 0: 
        return False
    
    if n % 2 != 0: 
        return False
    
    return isPowerOfTwo(n=n/2)

n = 65536
print(f"Is {n} a power of two? {isPowerOfTwo(n)}")