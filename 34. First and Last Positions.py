"""
Leetcode Problem 34
Find First and Last Position of Element in Sorted Array
"""

# first naive solution
# two pointers
# works but slow
def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # first check if array is empty
    size = len(nums)
    if size == 0: 
        return [-1,-1]
    
    # check array boundry values, if target is not between them
    # we know to return [-,1,-1]
    if target < nums[0] or target >  nums[size-1]: 
        return [-1,-1]
    
    p1, p2 = None, None
    
    for i in range(size): 
        if target == nums[i]: 
            p1 = i
            break
    
    if p1 is None: 
        return [-1,-1]
    
    for i in range(p1,size): 
        if target != nums[i]: 
            p2 = i-1
            break
        if i == size-1: 
            p2 = i
    
    return [p1,p2]

# Binary Search Method
# Guarantees O(logn) runtime 
def searchRangeBinarySearch(nums, target): 
    result = [-1,-1]
    high=len(nums)-1
    
    # first index flag indicates if we are trying to find the first position or the 
    # last position. Array is split accordingly in binary search. 
    result[0] = binarySearch(arr=nums, low=0, high=high, target=target, first_index=True)
    result[1] = binarySearch(arr=nums, low=0, high=high, target=target, first_index=False)
    
    return result    

def binarySearch(arr, low, high, target, first_index):
    index = -1 
    
    while low <= high: 
        mid = int((low + high)/2)
        
        if arr[mid] == target: 
            index = mid
            if first_index: 
                high = mid - 1
            else: 
                low = mid + 1

        elif target < arr[mid]: 
            high = mid -1
        
        else: 
            low = mid + 1
    
    return index

nums = [0]
target = 8
print(f"First and Last Positions are {searchRange(nums=nums, target=target)}")
print(f"Fast Binary Search Method Result is {searchRangeBinarySearch(nums=nums, target=target)}")