class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        
        i = 0
        maxcount = max(len(word1), len(word2)) - 1

        # return word1[i]

        while i <= maxcount:
            if i < len(word1):
                merged.append(word1[i])
            if i < len(word2):
                merged.append(word2[i])
            
            i += 1
        
        return ''.join(merged)



print(Solution().mergeAlternately("ab", "pqr"))