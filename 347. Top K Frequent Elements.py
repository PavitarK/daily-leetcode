"""
Leetcode Problem 347
Top K Frequent Elements
"""

# O(n) approach use bucket sort. Parse the given list and count 
# how many instances of each number in a dict. 
# Then organize into array of size nums
# parse array backwards for k elements and return most frequent values


def topKFrequent(nums: list[int], k: int) -> list[int]:
    count = {}
    bucket = [[] for i in range(len(nums) + 1)]
    out = []

    for num in nums: 
        count[num] = count.get(num,0) + 1
    
    for c,v in count.items(): 
        bucket[v].append(c)
    
    for i in range(len(nums),0,-1): 
        for val in bucket[i]:
            out.append(val)
            if len(out) == k: 
                return out

    return out

print(topKFrequent(nums=[1,1,1,1,1,2,2,2,3,2,1,3,3,3,3,3],k=2))