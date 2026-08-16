class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            tmp_key = [0] * 26
            for char in s:
                tmp_key[ord(char) - ord('a')] += 1
            anagrams[tuple(tmp_key)].append(s)
        
        ans = [value for value in anagrams.values()]
        return ans
