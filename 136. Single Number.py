"""
Leetcode Problem 136 
Single Number
""" 

# Brute Force, check every element and keep track of 
# what has already appeared once
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

# Use sorting (much faster)
# sort array then just parse once and see which
# number doesn't have a pair 
# don't need to parse the whole array

def singleNumber(nums): 
    nums.sort()

    for number in range(0,len(nums),2):
        # if reached end of list it must be the last element
        if number == len(nums)-1: 
            return nums[number]
        
        if nums[number] != nums[number+1]:
            single = nums[number]
            break
            
    return single