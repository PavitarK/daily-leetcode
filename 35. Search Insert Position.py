"""
Leetcode problem 35 
Search Insert Position
""" 

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    for index in range(len(nums)): 
        
        # if target is found return index or if found higher target
        if nums[index] >= target: 
            return index
            
    # if target is not found return the end of the list
    return len(nums)
    
            
        
if __name__ == "__main__": 
    nums = [1,3,5,6]
    target = 2
    result = searchInsert(nums=nums, target=target)
    print(f"Final Answer = {result}")
    
    
    