"""
Leetcode Problem 1071
Greatest Common Divisor of Strings
"""
import math 

def gcdOfStrings(str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)
    gcd = math.gcd(len1,len2)
    compare = ""
    t = str1[:gcd]
    
    # Check str1 
    div = len1/gcd
    while div > 0: 
        compare += t
        div -= 1
    
    if compare != str1: 
        return ""
    
    # Check str 2
    compare = ''
    div = len2/gcd
    while div > 0: 
        compare += t
        div -= 1
    
    if compare != str2: 
        return ""

    return t
    
def cleversol(str1: str, str2: str) -> str:
    if str1 + str2 == str2 + str1: 
            return str1[:math.gcd(len(str1),len(str2))] 
        
    return ""