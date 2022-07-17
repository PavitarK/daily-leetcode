"""
Leetcode problem 11 
Container with Most Water
""" 
# Works but too slow
# This iterates over the list O(n^2)
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
    
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    result = containerWithMostWater(height=height)
    print(f"Max Area = {result}")