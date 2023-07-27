"""
Leetcode Problem 383
Ransom Note
"""
# This solution is faster because we don't bother checking the rest of the
# magazine if even one letter doesn't exist.
# Beats 89% of submissions
def canConstructFast(ransomNote: str, magazine: str) -> bool:
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    
    for i in ransomNote:     
        if i in magazine: 
            magazine.remove(i)
        else: 
            return False
    
    return True

# Slow solution
# Beats 50% of submissions
def canConstruct(ransomNote: str, magazine: str) -> bool:
    note_len = len(ransomNote) 
    mag_len = len(magazine)
    
    if note_len > mag_len: 
        return False
    
    ransomNote = list(ransomNote)
    magazine = list(magazine)
    
    for i in magazine:     
        if i in ransomNote: 
            ransomNote.remove(i)
            if len(ransomNote) == 0: 
                return True
    
    return False

print(canConstruct(ransomNote="a",magazine="aab"))
print(canConstructFast(ransomNote="a",magazine="aab"))
