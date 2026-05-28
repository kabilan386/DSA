from typing import List
nums = [10, 20, 30]

numIteration = list(nums)

for i , value in enumerate(numIteration):
    if value == 20:
        del nums[i]



# nums.remove(20)

print(nums)


# nums = [10, 20, 30]

# del nums[1]

# print(nums)


# nums = [10, 20, 30]

