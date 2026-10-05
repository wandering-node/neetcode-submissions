class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''
        for char in s:
            if char.isalnum():
                clean_s += char
        for i in range(len(clean_s)//2):
            if clean_s[i].lower() != clean_s[-i-1].lower():
                return False
        return True