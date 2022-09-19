"""
LeetCode 521
Longest Uncommon Subsequence 1
"""

def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    if a == b: 
        return -1 
    else:
        return max(len(a), len(b))
        

a = "ccc"
b = "aaa"        
print(f"Longest Uncommon Subsequence is {findLUSlenght(a,b)}")