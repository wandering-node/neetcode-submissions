class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}

        def dfs(n):
            if n < 0:
                return -1
            if n in dp:
                return dp[n]
            min_path = float('inf')
            for num in coins:
               res = dfs(n - num)
               if res != -1:
                   min_path = min(min_path, res)
            dp[n] = min_path + 1 if min_path != float('inf') else -1
            return dp[n]
        return dfs(amount)