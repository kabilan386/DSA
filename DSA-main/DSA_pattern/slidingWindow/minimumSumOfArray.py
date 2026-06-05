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