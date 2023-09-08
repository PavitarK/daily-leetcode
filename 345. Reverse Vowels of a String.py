"""
Leetcode Problem 345
Reverse Vowels of a String
"""

def reverseVowels(s: str) -> str:
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    s = list(s)
    flip = []
    
    for letter in s: 
        if letter in vowels: 
            flip.append(letter)

    for i in range(len(s)): 
        if s[i] in vowels: 
            s[i] = flip[-1]
            flip.pop(-1)
        if len(flip) == 0:
            return ''.join(s)
    
# Two pointer solution    
def reverseVowelsFast(s: str) -> str: 
    # make vowels a set, it is much faster to check than a list
    # set makes searching O(1) while a list would be O(n)
    vowels = {'a','e','i','o','u','A','E','I','O','U'}
    front = 0 
    s = list(s)
    back = len(s)-1
    
    while front < back: 
        # find next vowel from front
        if s[front] in vowels and s[back] in vowels: 
            s[front], s[back] = s[back], s[front]
            front +=1
            back -=1
        else: 
            if s[front] not in vowels: 
                front +=1
            if s[back] not in vowels: 
                back -=1
    
    return ''.join(s)
    
print(reverseVowelsFast(s='wowee'))