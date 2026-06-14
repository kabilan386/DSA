# Question: Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# Description: The majority element is the element that appears more than n/2 times in the array. This means that it will always be the most frequent element in the array.


def majorityElement(nums):
    hashmap = {}
    majority = len(nums) // 2

    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
        else:
            hashmap[num] = 1
        
        if hashmap[num] > majority:
            majority = hashmap[num]
            return num
    
    return -1

print(majorityElement([2,2,1,1,1,2,2]))


# # Explanation:
# 1. We initialize an empty dictionary called `hashmap` to store the count of each element in the input array `nums`.
# 2. We calculate the majority threshold by dividing the length of the input array by 2 and storing it in the variable `majority`.
# 3. We iterate through each number in the input array `nums`. For each number, we check if it is already present in the `hashmap`. If it is, we increment its count by 1. If it is not present, we add it to the `hashmap` with a count of 1.
# 4. After updating the count for the current number, we check if its count exceeds the majority threshold. If it does, we update the `majority` variable to the current count and return the current number as the majority element.
# 5. If we finish iterating through the array without finding a majority element (which should not happen according to the problem statement), we return -1 as a fallback.  


# Time and Space Complexity:
# - Time Complexity: O(n), where n is the number of elements in the input array
# - Space Comlexity: O(1), since the majority element will always be the most frequent element, we can optimize the space complexity to O(1) by using a variable to keep track of the current majority element and its count instead of using a hashmap.