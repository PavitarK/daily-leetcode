"""
Leetcode Problem 66
Plus One
"""

def plusOne(digits: list) -> list: 
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    count = 0
    # if last digit is 9 incremement next value of array
    if digits[-1] == 9: 
        
        # count how many consecutive 9's there are from end of array
        for i in reversed(digits):
            if i == 9: 
                count = count + 1 
            else: 
                break
        
        # if all 9's insert a 1 at front of array
        if count >= len(digits):
            digits.insert(0,1)
        # else increment lowest non-nine number by 1
        else: 
            digits[-(count+1)] = digits[-(count+1)] + 1
        
        # all nine's below become 0
        n = count
        while n > 0: 
            digits[-n] = 0
            n = n - 1
    
    # if not 9 as lowest digit simply incrememnt it by 1    
    else: 
        digits[-1] = digits[-1] + 1
        
    return digits

#simple method convert to integer, add one and convert to string
def plusOneListToInt(digits: list) -> list: 
    return [int(a) for a in str((int(''.join(str(e) for e in digits))+1))]
    
if __name__ == "__main__":
    digits = [9,9]
    # result = plusOne(digits=digits) 
    # print(f"Final Answer = {result}")
    result = plusOneListToInt(digits)
    print(f"Final Answer = {result}")