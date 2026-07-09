
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        ans = right + 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
    

# print(Solution().searchInsert([1,3,5,6], 5))  # Output: 2
# print(Solution().searchInsert([1,3,5,6], 2))  # Output: 1
print(Solution().searchInsert([1,3,5,6], 7))  # Output: 4
# print(Solution().searchInsert([1,3,5,6], 0))  # Output: 0
