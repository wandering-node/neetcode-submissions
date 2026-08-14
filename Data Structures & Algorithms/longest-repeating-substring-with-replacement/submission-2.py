class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        l = 0
        max_cnt = 0
        longest = 0
        
        for r in range(len(s)):
            # 1. Add current character to window
            count[s[r]] += 1
            max_cnt = max(max_cnt, count[s[r]])
            
            # 2. Shrink window if invalid
            while (r - l + 1) - max_cnt > k:
                count[s[l]] -= 1
                l += 1
            
            # 3. Update result
            longest = max(longest, r - l + 1)
            
        return longest