# Question : Sort the array using insertion sort.
# Description : Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time.


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    arr = [1, 3, 5, 4, 2]
    print(insertion_sort(arr))


# Loops
# for i in range(1, len(arr)) - this loop is used to iterate through the array
# while j >= 0 and key < arr[j] - this loop is used to shift the elements to the right


# Time and space complexity
# Time complexity : O(n)    
# Space complexity : O(1)