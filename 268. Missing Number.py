"""
Leetcode Problem 268
Missing Number
"""

def missingNumber(nums: list) -> int: 
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    highest_value = nums[-1]
    
    for value in range(highest_value): 
        if nums[value] != value: 
            return value
    
    return highest_value + 1
    

if __name__ == "__main__":
    nums = [0]
    result = missingNumber(nums=nums)
    
    print(f"Final Answer = {result}")