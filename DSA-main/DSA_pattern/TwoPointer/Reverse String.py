from typing import List 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        size = len(s) - 1

        while i < size:
            s[i] , s[size] = s[size] , s[i]
            i += 1
            size -= 1

        return s
    

print(Solution().reverseString(["h","e","l","l","o"]))