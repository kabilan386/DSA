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