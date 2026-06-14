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
        