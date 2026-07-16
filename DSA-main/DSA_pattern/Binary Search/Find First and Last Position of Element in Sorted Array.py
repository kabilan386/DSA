from typing import List

# Explanation: The code defines a class Solution with a method searchRange that takes a sorted list of integers nums and a target integer. It returns the starting and ending positions of the target in the list. If the target is not found, it returns [-1, -1]. The method uses two helper functions, find_f and find_l, to perform binary searches for the first and last occurrences of the target, respectively. The overall time complexity is O(log n) and space complexity is O(1).

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_f():
            left, right = 0,len(nums) - 1 
            ans = -1
            while left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    ans = mid
                    right = mid-1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid +1
            return ans
        def find_l():
            left, right =0, len(nums) - 1 
            ans = -1
            while left<=right:
                mid = (left + right)//2
                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid +1
            return ans
        return[find_f(),find_l()]    

        
print(Solution().searchRange([5,7,7,8,8,10], 8)) # Output: [3, 4]

# Time Complexity: O(log n) for both find_f and find_l functions, so overall O(log n)
# Space Complexity: O(1) since we are using constant space for variables.