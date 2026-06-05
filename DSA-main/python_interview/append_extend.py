a = [1, 2]

a.append([3, 4])
# [1, 2, [3, 4]]

a.extend([5, 6])
# [1, 2, [3, 4], 5, 6]

print(a)

a.pop(0)

print(a)