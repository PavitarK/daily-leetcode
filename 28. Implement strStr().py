"""
Leetcode Problem 28 
Implement strStr()
"""

def strStr(haystack, needle): 
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    needle_length = len(needle)
    
    # edge case: if needle is empty return 0 
    if needle_length == 0: 
        return 0 
    
    # return index of first occurence of needle in haystack
    # first check if window is larger than the haystack
    if needle_length > len(haystack): 
        return -1
    
    for i in range(len(haystack)):
        if haystack[i:i+needle_length] == needle: 
            return i
    
    return -1
    

if __name__ == "__main__": 
    needle = "fun"
    haystack = "superduperfuntimescodingyaaas"
    result = strStr(needle=needle, haystack=haystack)
    
    print(f"Final Answer = {result}")
