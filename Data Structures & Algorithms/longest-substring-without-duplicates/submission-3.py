class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_dict = {}
        max_len = 0
        l = 0
        r = 0
        for i in range(len(s)):
            if s[i] in str_dict and str_dict[s[i]] >= l:
                l = str_dict[s[i]] + 1
            r += 1
            str_dict[s[i]] = i
            max_len = max(max_len, r-l)
        return max_len