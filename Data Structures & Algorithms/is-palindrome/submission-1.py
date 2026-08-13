class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure_s = ''
        # extract the alphanumerical characters in the string
        for char in s:
            if char.isalnum():
                pure_s += char
            else:
                continue
        print(pure_s)
        if pure_s:
            for i in range(len(pure_s)//2 + 1):
                if pure_s[i].lower() != pure_s[-i-1].lower():
                    return False
        return True

