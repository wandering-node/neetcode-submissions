class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""
        for char in s:
            if char.isalnum():
                clean_s += char.lower()
        l = 0
        r = len(clean_s) - 1
        while l < len(clean_s) // 2:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        return True
