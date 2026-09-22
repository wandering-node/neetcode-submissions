class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        dp = {}
        def dfs(idx1, idx2):
            if idx1 >= l1 or idx2 >= l2:
                dp[(idx1, idx2)] = 0
                return 0
            if text1[idx1] == text2[idx2]:
                if (idx1 + 1, idx2 + 1) not in dp:
                    dp[(idx1 + 1, idx2 + 1)] = dfs(idx1 + 1, idx2 + 1)
                dp[(idx1, idx2)] = dp[(idx1 + 1, idx2 + 1)] + 1
                return dp[(idx1, idx2)]
            else:
                if (idx1, idx2 + 1) not in dp:
                    dp[(idx1, idx2 + 1)] = dfs(idx1, idx2 + 1)
                if (idx1 + 1, idx2) not in dp:
                    dp[(idx1 + 1, idx2)] = dfs(idx1 + 1, idx2)
                return max(dp[(idx1, idx2 + 1)], dp[(idx1 + 1, idx2)])
        return dfs(0, 0)