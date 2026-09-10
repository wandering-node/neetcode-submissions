class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}

        def dfs(n):
            if n in dp:
                return dp[n]
            if n < 0:
                return -1
            minum = float("inf")
            for coin in coins:
                if dfs(n - coin) != -1:
                    minum = min(dfs(n - coin), minum)
                dp[n] = minum + 1 if minum != float("inf") else -1
            return dp[n]
        return dfs(amount)