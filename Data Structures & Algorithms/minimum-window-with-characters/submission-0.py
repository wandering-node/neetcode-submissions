class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        countT, window = {}, {}
        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        res = [-1, -1]
        resLen = float("inf")
        l = 0
        have, need = 0, len(countT)
        for r in range(len(s)):
            if s[r] in countT:
                window[s[r]] = 1 + window.get(s[r], 0)
                if window[s[r]] == countT[s[r]]:
                    have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                if s[l] in countT:
                    window[s[l]] -= 1
                    if window[s[l]] < countT[s[l]]:
                        have -= 1
                l += 1
        l, r = res
        return s[l: r + 1]
