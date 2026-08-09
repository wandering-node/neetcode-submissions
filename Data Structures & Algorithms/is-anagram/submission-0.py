class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)
        for s_l in s:
            dict_s[s_l] += 1
        for t_l in t:
            dict_t[t_l] += 1
        return dict_t == dict_s

