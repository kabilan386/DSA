def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    hashmap = {}
    for i in range(len(s1)):
        hashmap[s1[i]] = hashmap.get(s1[i], 0) + 1
    for i in range(len(s2)):
        if s2[i] not in hashmap:
            return False
        hashmap[s2[i]] -= 1
    for i in hashmap:
        if hashmap[i] != 0:
            return False
    return True

print(anagram("listen", "silent"))