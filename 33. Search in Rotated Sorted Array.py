def search(nums, target: int) -> int:
        l,r = 0, len(nums)-1 
        result = -1 

        while l<=r: 
            m = (l+r) // 2
            if nums[m] == target: 
                return m

            if nums[m] >= nums[l]: 
                # then we are in the left sorted array
                if nums[l] <= target < nums[m]: 
                    r = m - 1
                else: 
                    l = m + 1
            else: 
                # then we are in the right sorted array
                if nums[m] < target <= nums[r]: 
                    l = m + 1
                else: 
                    r = m - 1
        
        return result 