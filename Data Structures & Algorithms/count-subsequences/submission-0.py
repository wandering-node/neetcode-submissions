class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(t):
                memo[(i, j)] = 1
                return 1
            if i <= len(s) - 1 and j <= len(t) - 1:
                if s[i] == t[j]:
                    memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
                else:
                    memo[(i, j)] = dfs(i + 1, j)
                return memo[(i, j)]
            else:
                return 0
        return dfs(0, 0)