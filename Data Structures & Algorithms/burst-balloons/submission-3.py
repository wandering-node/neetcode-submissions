from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]

        @cache
        def dp(i, j):
            if i == j - 1:
                return 0

            total = 0
            # burst k last
            for k in range(i + 1, j):
                coins = dp(i, k) + dp(k, j) + a[i] * a[k] * a[j]
                total = max(total, coins)
            return total

        return dp(0, len(nums) + 1)
