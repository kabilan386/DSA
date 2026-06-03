value = 'aaabcdbcffvvgee'

def findsecondnonduplicate(value):
    hashmap = {}
    for i in range(len(value)):
        hashmap[value[i]] = hashmap.get(value[i], 0) + 1
    
    print(hashmap)
    count = 0
    for (key , value) in hashmap.items():
        if value == 1:
            count += 1
            if count == 2:
                return key
    return -1

print(findsecondnonduplicate(value))