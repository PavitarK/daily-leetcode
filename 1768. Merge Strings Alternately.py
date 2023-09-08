"""
Leetcode Problem 1768
Merge Strings Alternately
"""

def mergeAlternately(word1: str, word2: str) -> str:
        mergedString = ''
        ptr = 0 
        minLen = min(len(word1), len(word2))

        while ptr < minLen: 
            mergedString += word1[ptr]
            mergedString += word2[ptr]
            ptr +=1

        if len(word2) > ptr: 
            mergedString += word2[ptr:]

        if len(word1) > ptr: 
            mergedString += word1[ptr:]

        return mergedString