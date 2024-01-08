
# roated atleast once so left sorted will always be larger than right sorted unelss sorted n times
# start at middle check left and right
# if middle is less than left we know rotated less than n times, so smaller numbers in left sorted arrary
# if middle is greater than left we know the left side is the smaller sorted array. 

# if middle value is part of left or right sorted array
# do this by comparing with lowst element 
# if middle is less than everything to the left we know we're at the lowest of that sorted portion so check left
# if middle is greater than everything to the left we know we are at the end of a sorted portion so check right. 

# --> variation of binary search
# O(logn) solution

def findMin( nums: [int]) -> int:
    l , r = 0, len(nums)-1 
    result = nums[0]

    while l <= r: 
        mid = (l+r) // 2 
        print(mid)
        if nums[l] <= nums[r]: 
            return min(result, nums[l])
        if nums[mid] >= nums[l]: 
            result = min(nums[l], result)
            l = mid + 1
        else: 
            result = min(result, nums[mid])
            r = mid - 1
        
    return result


        
        