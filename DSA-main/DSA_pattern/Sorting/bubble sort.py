# Question : Sort the array using bubble sort.
# Description : Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


a = [1, 3, 5, 4, 2]

print(bubble_sort(a))

# Loops
# for i in range(len(arr) - 1) - this loop is used to iterate through the array
# for j in range(len(arr) - 1) - this loop is used to find the longest substring without repeating characters


# Time and space complexity
# Time complexity : O(n)
# Space complexity : O(1)