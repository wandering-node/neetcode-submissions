class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # from collections import defaultdict
        # dict_s = defaultdict(int)
        # dict_t = defaultdict(int)
        # for s_l in s:
        #     dict_s[s_l] += 1
        # for t_l in t:
        #     dict_t[t_l] += 1
        # return dict_t == dict_s

        # solution 2:
        # easy egde case
        if len(s) != len(t):
            return false
        # empty clean list for 26 letters as a counter
        count = [0] * 26
        # loop through all the letters in s & t
        for i, j in zip(s, t):
            # get occurance of letters in s
            count[ord(i) - ord('a')] += 1 
            # cancel occurance of letters in t
            count[ord(j) - ord('a')] -= 1
        return count == [0] * 26 

