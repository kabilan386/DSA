from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]

            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            
            end = nums[i]

            if start == end:
                intervals.append(str(start))
            else:
                intervals.append(str(start) + "->" + str(end))

            i += 1
            

        return intervals


# print(Solution().summaryRanges([0,1,2,4,5,7]))
print(Solution().summaryRanges([0,2,3,4,6,8,9]))

