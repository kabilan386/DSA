
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        window = set()

        for right in range(len(nums)):
            if len(window) > k:
                value = nums[left]
                window.remove(value)
                left += 1
           
            if nums[right] in window:
                return True            

            value = nums[right]
            window.add(value)          

        return False
    
# print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
# print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))
# print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))