# Question : Find the leaders in an array.
# Description : An element is a leader if it is greater than all the elements to its right.

def leaderArray(arr):
    output = []
    
    for i in range(len(arr) - 1, -1 , -1):
        length = len(output)
        if length == 0:
            output.append(arr[i])
        elif arr[i] > output[len(output) - 1]:
            output.append(arr[i])
    
    return output[::-1]


arr = [16, 17, 4, 3, 5, 2]

print(leaderArray(arr))


# Loops
# for i in range(len(arr) - 1, -1 , -1) - this loop is used to iterate through the array from right to left
# if arr[i] > output[len(output) - 1] - this condition is used to check if the element is greater than the previous element

# Time and space complexity
# Time complexity : O(n)
# Space complexity : O(1)