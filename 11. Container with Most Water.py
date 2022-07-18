"""
Leetcode problem 11 
Container with Most Water
""" 
# Works but too slow
# This iterates over the list O(n^2)
# Approach: Iterate over every possible container to find largest area
from turtle import right


def containerWithMostWater(height: list) -> int: 
    max_area = 0
    
    for start in range(len(height)): 
        for end in range(start+1,len(height)): 
            if height[start] > height[end]: 
                max_height = height[end]
            else: 
                max_height = height[start]
                
            area = max_height * (end-start)
            
            if area > max_area:
                max_area = area
    
    return max_area
    
#   Approach: Use two pointers, one starting from the left 
#   one from the right (i.e at maximum container width). Then
#   move pointer that is at a lower height. Then find the area and
#   check if the max area has been beaten.
#   In other words check if the reduction in width is made up for
#   in height. O(1) Time complexity, only need to parse list once!      
def containerWithMostWaterFast(height: list) -> int: 
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1 
    right_wall = height[right]
    left_wall = height[left]
    
    # set initial max area
    max_area = getArea(left_wall=left_wall, right_wall=right_wall, distance=(right-left))
        
    while right-left > 1: 
        if height[left] < height[right]: 
            left += 1
            if height[left] > right_wall or height[left] > left_wall:
                left_wall = height[left]
                area = getArea(left_wall=left_wall, right_wall=right_wall, distance=(right-left))
                if area > max_area: 
                    max_area = area
        else: 
            right -=1
            if height[right] > right_wall or height[right] > left_wall: 
                right_wall = height[right]
                area = getArea(left_wall=left_wall, right_wall=right_wall, distance=(right-left))
                if area > max_area: 
                    max_area = area
            
    return max_area 


def getArea(left_wall, right_wall, distance):
    if right_wall > left_wall: 
        max_area = left_wall * distance
    else: 
        max_area = right_wall * distance 
        
    return max_area        
        
 
if __name__ == "__main__":
    height = [4,2,3,4,5,1]
    result = containerWithMostWater(height=height)
    result_2 = containerWithMostWaterFast(height=height)
    print(f"\nMax Area = {result}")
    print(f"Max Area Fast = {result_2}")