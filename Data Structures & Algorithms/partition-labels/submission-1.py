class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {char: idx for idx, char in enumerate(s)}
        ans = []
        l = r = 0
        for idx, char in enumerate(s):
            if idx_map[char] != idx:
                r = max(r, idx_map[char])
            elif idx_map[char] == idx and r <= idx_map[char]:
                ans.append(r - l + 1)
                l = r + 1
                r = l
            else:
                continue
        return ans