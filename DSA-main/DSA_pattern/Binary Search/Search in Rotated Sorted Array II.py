# Explanation: The provided code implements a solution to search for a target value in a rotated sorted array using a modified binary search algorithm. The algorithm efficiently narrows down the search space by determining which half of the array is sorted and adjusting the search boundaries accordingly.

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            
            if nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:
                if target>=nums[left]and target <= nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target<=nums[right]and target >= nums[mid]:
                    left=mid+1
                else:
                    right=mid-1
        return False


print(Solution().search([2,5,6,0,0,1,2], 0))  # Output: True  


# Time Complexity: O(log n) - The algorithm performs a binary search, which divides the search space in half with each iteration, leading to logarithmic time complexity.
# Space Complexity: O(1) - The algorithm uses a constant amount of space for variables, regardless of the input size.
