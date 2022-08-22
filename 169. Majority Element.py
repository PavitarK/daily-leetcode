"""
Leetcode Problem 169
Majority Element

"""

def majorityElement(nums): 
    """
    Brute force solution
    Uses dictionary to track elements and counts how many times
    one element is seen in given list
    """
    tracker = {}
    majority = int(len(nums)/2 + 1)
    
    for i in nums: 
        tracker[i] += 1
            
        if tracker[i] == majority:
            return i 
        
        print(tracker)
        
        
print(f"The majority element is {majorityElement(nums=[2,2,1,1,1,2,2])}")