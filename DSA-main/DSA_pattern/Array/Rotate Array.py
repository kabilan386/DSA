class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n   # Handle cases where k is greater than n
        nums[:] = nums[-k:] + nums[:-k]  # Rotate the array in place
        return nums


print(Solution().rotate([1,2,3,4,5,6,7], 3))  # Output: [5,6,7,1,2,3,4]