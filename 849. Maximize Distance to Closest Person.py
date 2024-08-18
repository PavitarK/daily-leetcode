# Problem 849 Leetcode
# Google Mock Assessment 
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # two pointers
        # max distance = 0
        # start at 0 with left pointer and l+1 with right
        # if right pointer = 1
            # get the diff between indices and track max
            # then left pointer gets right pointer and right is left+1 again
            # continute until right > len(seats)\
            
        # if max = 0 no second filled seat is found
            # return len(seats) 
            
        max_distance = 0 
        n = len(seats)
        left = 0
        
        while left < n-1:
            if seats[left] != 1:  
                max_distance +=1 
                left +=1
            else: 
                break

        while left < n-2: 
            if seats[left] == 1:
                right = left + 1
                while right <= n-1:
                    if right == n-1 and seats[right] != 1: 
                        distance = right - left
                        max_distance = max(max_distance, distance)
                        left = right
                    if seats[right] == 1:
                        distance = (right - left) / 2
                        max_distance = max(max_distance, distance)
                        left = right
                         
                    right +=1
            else: 
                left +=1
                

        return int(max_distance)