class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        
        for i in range(len(s)):
            l = r = i
            while r + 1 < len(s) and s[r] == s[r+1]:
                cnt += 1
                r += 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            
        return cnt
