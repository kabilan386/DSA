from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        if j ==  -1:
            return
        

        for i in range(j + 1,len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i] = nums[i]  , nums[j]
                j += 1

            
# arr = [0,1,0,3,12]
arr = [2,1]

Solution().moveZeroes(arr)

print(arr)

