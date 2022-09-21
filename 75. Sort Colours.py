"""
Leetcode Problem 75
Sort Colours
"""

def sortColours(nums): 
    high = len(nums)
    if high > 0: 
        quickSort(nums,low=0,high=high-1)
    else: 
        return None
    
def quickSort(nums, low, high): 
    if low < high:
        pi = partition(nums, low, high)
        quickSort(nums, low, pi-1)
        quickSort(nums,pi+1, high)
    
    return None

def partition(nums, low, high):
    pivot = nums[high]
    i = low-1
    
    print(pivot)
    for j in range(low,high): 
        if nums[j] < pivot: 
            i += 1
            swap(nums,i,j)
    
    i += 1
    swap(nums,i,high)
    print(colours)
    return i
    
def swap(nums,i,j): 
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp

colours = [10,1,2,1,9]
print(colours)
sortColours(colours)
print(colours)