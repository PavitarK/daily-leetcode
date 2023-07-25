"""
Leetcode Problem 15
3Sum
"""


def threeSum(nums: list[int]) -> list[list[int]]:
    length = len(nums)
    result = []
    pairs = []
    
    nums.sort()
    
    for s in range(length-2): 
        i = s+1 
        k = length-1
        
        while i<k and i>s and k<length: 
            sum = nums[s] + nums[i] + nums[k]
            if sum == 0:
                r = [nums[s],nums[i],nums[k]]
                if r not in result:  
                    result.append(r)
                i = i + 1
            elif sum > 0: 
                k = k - 1
            else: 
                i = i + 1
        
    print(result)

    return result 

#
# Works but too slow on large complex integer sets. 
#
def threeSumSlow(nums: list[int]) -> list[list[int]]:
    
    length = len(nums)
    result = []
    pairs = []
    
    #check that array is valid
    if length < 3: 
        return result
    
    start = 0
    while start < length: 
        i = start+1
        while i < length:
            if [nums[start], nums[i]] in pairs: 
                None
            else:
                pairs.append([nums[start], nums[i]])
                for l in range(length):
                    if l != start and l != i:  
                        if nums[start] + nums[i] + nums[l] == 0:
                            r = [nums[start],nums[i],nums[l]]
                            r.sort()
                            if r not in result:
                                result.append(r)
            i = i + 1
        start = start + 1
     
    print(result)
    
    return result

threeSumSlow([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])