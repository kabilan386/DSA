class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        ans = nums[left]
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= nums[right]:
                ans = min(nums[mid], ans)
                right = mid - 1
            else:
                ans = min(nums[right], ans)
                left = mid + 1

        return ans


print(Solution().findMin([3,4,5,1,2]))  # Output: 1