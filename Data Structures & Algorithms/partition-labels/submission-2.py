class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {char: idx for idx, char in enumerate(s)}
        ans = []
        l = r = 0
        for idx, char in enumerate(s):
            r = max(r, idx_map[char])
            if r == idx:
                ans.append(r - l + 1)
                l = r + 1
                r = l
           
        return ans