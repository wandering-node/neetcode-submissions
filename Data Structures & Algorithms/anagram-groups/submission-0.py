class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_dict = {}
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            if (count_key:=tuple(count)) in ana_dict:
                ana_dict[count_key].append(s)
            else:
                ana_dict[count_key] = [s]
        ans = []
        for key in ana_dict.keys():
            ans.append(ana_dict[key])
        return ans
