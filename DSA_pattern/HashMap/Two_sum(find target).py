def two_sum(arr, target):
    hashmap = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[arr[i]] = i
    return []

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))