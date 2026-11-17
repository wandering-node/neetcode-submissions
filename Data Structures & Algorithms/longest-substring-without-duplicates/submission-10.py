class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l = 0
        pre_idx = {}
        for r, char in enumerate(s):
            if char in pre_idx:
                l = max(l, pre_idx[char] + 1)
                maxLen = max(maxLen, (r - l + 1))
                pre_idx[char] = r
            else:
                pre_idx[char] = r
                maxLen = max(maxLen, (r - l + 1))
        return maxLen
