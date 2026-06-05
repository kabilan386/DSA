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