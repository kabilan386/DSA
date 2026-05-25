from collections import Counter

def canConstruct(ransomNote, magazine):
    count = Counter(magazine)
   

    for ch in ransomNote:
        if count[ch] == 0:
            return False

        count[ch] -= 1
        print(count)

    return True

print(canConstruct("a", "aa"))