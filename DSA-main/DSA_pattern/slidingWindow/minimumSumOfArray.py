# Question : Find the minimum length of the subarray whose sum is greater than or equal to target. If no such subarray exists, return 0.


arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

def minSubArray(nums , target):
    left = 0
    right = 0
    subSum = 0
    minimum = []

    while right < len(nums):
        subSum += nums[right]

        while subSum >= target:
            minimum.append(right - left + 1)
            subSum -= nums[left]
            left += 1

        right += 1
    
    return minimum








print(minSubArray(arr , k))


# Loops
# while right < len(nums) - this loop is used to iterate through the array
# while subSum >= target - this loop is used to find the minimum length of the subarray



# Time and space complexity
# Time complexity : O(n)
# Space complexity : O(1)