import string
def isPalindrome( s: str) -> bool:
    # Replace all spaces and remove punctuation
    # convert upper case to lowercase
    # two pointers first and last
    # while first <= last check equal
    # first ++ 
    # last -- 
    s = s.replace(" ", "")
    s = s.translate(str.maketrans('', '', string.punctuation))
    s = s.lower()
    
    first = 0 
    last = len(s)-1
    while first <= last: 
        if s[first] != s[last]: 
            return False
        first +=1 
        last -=1
    return True

print(isPalindrome(s="abccba"))