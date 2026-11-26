class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        S = sum(nums)

        if abs(target) > S:
            return 0

        dp = [[0] * (2 * S + 1) for _ in range(n + 1)]
        dp[0][S] = 1

        for i, num in enumerate(nums):
            for j in range(2 * S + 1):
                if dp[i][j] == 0:
                    continue

                dp[i + 1][j + num] += dp[i][j]
                dp[i + 1][j - num] += dp[i][j]

        return dp[n][target + S]