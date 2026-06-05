from typing import List

nums = [1,12,-5,-6,50,3]

k = 4

def findMaxAverage(nums, k):
        
    window_sum = sum(nums[:k])

    maximum_sum = window_sum

    for i in range(k,len(nums)):
        window_sum += nums[i] - nums[i-k]
        maximum_sum = max(maximum_sum , window_sum)

    return maximum_sum / k 


print(findMaxAverage(nums,k))