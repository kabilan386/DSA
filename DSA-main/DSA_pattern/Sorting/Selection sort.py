# Question : Sort the array using selection sort.
# Description : Selection sort is a simple sorting algorithm that builds the final sorted array one item at a time.


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


a = [1, 3, 5, 4, 2]

print(selection_sort(a))

# Loops
# for i in range(len(arr)) - this loop is used to iterate through the array
# for j in range(i + 1, len(arr)) - this loop is used to find the minimum element


# Time and space complexity
# Time complexity : O(n^2)
# Space complexity : O(1)
