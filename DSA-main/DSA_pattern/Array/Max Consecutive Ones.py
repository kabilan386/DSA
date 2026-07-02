from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcount = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                maxcount = max(count, maxcount)
            else:
                count = 0

        return maxcount 

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))  # Output: 3

