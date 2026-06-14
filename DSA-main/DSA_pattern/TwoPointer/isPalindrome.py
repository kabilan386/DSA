# 125. Valid Palindrome
# Description: Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1
            
            while left < right and not s[right].isalnum():
                right -= 1

            if(s[left].lower() != s[right].lower()):
                return False
            left += 1
            right -= 1
        
        return True
        

print(isPalindrome("A man, a plan, a canal: Panama"))


# Explanation:
# 1. We initialize two pointers, `left` and `right`, to the start and end of the input string `s`, respectively.
# 2. We enter a loop that continues until the `left` pointer is less than the `right` pointer.
# 3. Inside the loop, we first check if the character at the `left` pointer is not alphanumeric. If it is not, we increment the `left` pointer to skip it.
# 4. We then check if the character at the `right` pointer is not alphanumeric. If it is not, we decrement the `right` pointer to skip it.
# 5. After skipping any non-alphanumeric characters, we compare the characters at the `left` and `right` pointers, ignoring case. If they are not equal, we return `False`, indicating that the string is not a palindrome.
# 6. If the characters are equal, we move both pointers towards the center by incrementing the `left` pointer and decrementing the `right` pointer.
# 7. If we exit the loop without finding any mismatched characters, we return `True`, indicating that the string is a palindrome.   

# Time and Space Complexity:
# - Time Complexity: O(n), where n is the length of the input string `s`.
# - Space Complexity: O(1), since we are using only a constant amount of extra space for the pointers and temporary variables.  