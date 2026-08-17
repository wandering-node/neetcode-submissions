class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        l = 0
        ans = 0
        seen = defaultdict(int)
        max_cnt = 0
        for r in range(len(s)):
            # ans = max(ans, (r - l + 1))
            seen[s[r]] += 1
            max_cnt = max(max_cnt, seen[s[r]])
            if r - l + 1 > max_cnt + k:
                seen[s[l]] -= 1
                l += 1
                
            ans = max(ans, (r - l + 1))
        return ans