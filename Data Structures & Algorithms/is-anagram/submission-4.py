class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            res[idx] += 1

        for char in t:
            idx = ord(char) - ord('a')
            res[idx] -= 1
        
        return res == [0] * 26