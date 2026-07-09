# Question : Search the target in the array using binary search.
# Description : Binary search is a search algorithm that searches for a target value in a sorted array.


def binarySearch(arr,target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print("mid",mid,'left',left,'right',right)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

print(binarySearch([1,2,3,4,5], 5))

# loops
# while left <= right - this loop is used to iterate through the array


# Time and space complexity
# Time complexity : O(log n)
# Space complexity : O(1)