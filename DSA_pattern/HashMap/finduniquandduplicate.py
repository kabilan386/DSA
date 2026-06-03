arr = [1, 3, 4, 6, 2, 3, 4, 5, 7]

def finduniquandduplicate(arr):
    hashmap = {}
    for i in range(len(arr)):
        hashmap[arr[i]] = hashmap.get(arr[i], 0) + 1
    
    duplicate = []
    unique = []
    for key,value in hashmap.items():
        if value == 1:
            unique.append(key)
        else:
            duplicate.append(key)
    return unique, duplicate

print(finduniquandduplicate(arr))