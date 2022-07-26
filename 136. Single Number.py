"""
Leetcode Problem 136 
Single Number
""" 
     
def singleNumber(nums): 
    once = []
    twice = []
    
    for number in nums: 
        if number in once: 
            twice.append(number)
            once.remove(number)
        else: 
            once.append(number)
            
    return once[0]