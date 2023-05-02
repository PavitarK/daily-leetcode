"""
Leetcode Problem 217 
Contains Duplicate
Given an integer array nums, 
return true if any value appears at least twice in the array, 
and return false if every element is distinct.
"""

def containsDuplicate(nums: list[int]) -> bool:
    length = len(nums)
    nums.sort()
    i = 0
    while i < length-1:
        if nums[i] == nums[i+1]:
            return True
        i = i + 1

    return False


