def groupanagram(arr):
    hashmap = {}
    
    for word in arr:
        
        key = ''.join(sorted(word))
        
        if key not in hashmap:
            hashmap[key] = []
        
        hashmap[key].append(word)
    
    return hashmap

print(groupanagram(["eat","tea","tan","ate","nat","bat"]))

# output : {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}

# Time and Space Complexity 
# Time : O(n * k log k) = O(n log n)
# Space : O(n * k) = O(n)

# 