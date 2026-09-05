class Solution:
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)):
            # odd length
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # print(f"odd {l}, {r}")
                cnt += 1
                l -= 1
                r += 1
            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1

        return cnt
