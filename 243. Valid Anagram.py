"""
Leetcode Problem 243
Valid Anagram
"""

def isAnagram(s: str, t: str) -> bool:
    length = len(s)
    if length == len(t): 
        s_sort = ''.join(sorted(s))
        t_sort = ''.join(sorted(t))
        if s_sort == t_sort: 
            return True
    return False

print(isAnagram(s='abcde', t='edcba'))