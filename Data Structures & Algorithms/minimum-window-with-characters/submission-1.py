class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = collections.Counter(t)
        need = len(countT)
        have = 0
        countSub = {}
        left = 0
        ans = ""
        ans_len = float("inf")
        for i in range(len(s)):
            if s[i] in countT:
                countSub[s[i]] = countSub.get(s[i], 0) + 1
                if countSub[s[i]] == countT[s[i]]:
                    have += 1
                while have == need:
                    if (i - left + 1) < ans_len:
                        ans = s[left: i + 1]
                        ans_len = i - left + 1
                    if s[left] in countT:
                        countSub[s[left]] -= 1
                        if countSub[s[left]] < countT[s[left]]:
                            have -= 1
                    left += 1
        return ans
                    
