# Question: Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# Description: You must write an algorithm that runs in O(n) time.

def longestConsecutive(nums):
    hashmap = set(nums)
    longest = 0

    for num in hashmap:
        if num - 1 not in hashmap:
            currentNum = num
            currentStreak = 1

            while currentNum + 1 in hashmap:
                currentNum += 1
                currentStreak += 1
            
            longest = max(longest,currentStreak)
    
    return longest


print(longestConsecutive([100,4,200,1,3,2]))


# # Explanation:
# 1. We first convert the input list `nums` into a set called `hashmap`. This allows for O(1) average time complexity for lookups.
# 2. We initialize a variable `longest` to keep track of the length of the longest consecutive sequence found so far.
# 3. We iterate through each number in the `hashmap`. For each number, we check if it is the start of a sequence by verifying that `num - 1` is not in the `hashmap`. If it is not present, it means that `num` is the beginning of a new sequence.
# 4. We then initialize `currentNum` to the current number and `currentStreak` to 1. We enter a while loop that continues as long as `currentNum + 1` is present in the `hashmap`. Inside the loop, we increment `currentNum` and `currentStreak` to count the length of the current consecutive sequence.
# 5. After exiting the while loop, we update `longest` with the maximum value between `longest` and `currentStreak`.
# 6. Finally, we return the value of `longest`, which represents the length of the longest consecutive elements sequence found in the input array.  


# Time and Space Complexity:
# - Time Complexity: O(n), where n is the number of elements in the input array
# - Space Complexity: O(n), where n is the number of unique elements in the input
        

