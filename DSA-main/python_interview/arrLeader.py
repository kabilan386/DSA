a = [16, 17, 4, 3, 5, 2]

arr = []

for i in range(len(a) - 1, -1, -1):
    if len(arr) == 0:
        arr.append(a[i])
    elif arr[-1] < a[i]:
        arr.append(a[i])

print(arr[::-1])