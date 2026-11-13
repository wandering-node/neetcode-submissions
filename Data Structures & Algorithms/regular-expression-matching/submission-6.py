from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            if (j < len(p) - 1 and p[j + 1] != "*") or (j == len(p) - 1):
                return i < len(s) and ((s[i] == p[j]) or p[j] == ".") and dfs(i + 1, j + 1)
            else:
                zero_match = dfs(i, j + 2)
                repeat_match = i < len(s) and (s[i] == p[j] or p[j] == ".") and dfs(i + 1, j)
                return zero_match or repeat_match
        return dfs(0, 0)
