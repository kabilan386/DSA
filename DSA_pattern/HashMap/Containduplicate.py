from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    strValue = set()

    for i in range(len(nums)):
        if nums[i] in strValue:
            return True
        strValue.add(nums[i])
    return False 

print(containsDuplicate([1, 2, 3, 1]))