"""
Leetcode 278
First Bad Version
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import math

### First Solution, faster than 50% of python submissions ###
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    prev = 0
    curr = math.ceil(float(n)/2)
    good = False
    
    while True:
        if not isBadVersion(curr): 
            add = math.ceil(abs(curr-prev)/2)
            prev = curr
            curr = curr + add 
            good = True
        else: 
            if prev == (curr - 1) and good: 
                return int(curr)
            sub = math.ceil((abs(curr-prev)/2))
            prev = curr
            curr = curr - sub
            good = False
            

### Cleaned up, faster than 76% of python submissions. ###           
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    prev = 0
    curr = math.ceil(float(n)/2)
    good = False
    
    while True:
        versionCheck = isBadVersion(curr)
        diff = math.ceil(abs(curr-prev)/2)
        if not versionCheck: 
            prev = curr
            curr = curr + diff # round up to nearest integer
            good = True
        else: 
            if prev == (curr - 1) and good: 
                return int(curr)
            prev = curr
            curr = curr - diff
            good = False