class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]
        memo = {}
        def dp(l, r):
            if (l, r) in memo:
                return memo[(l, r)]
            if r - l == 1:
                # no ballons in the middle
                return 0
            total = 0
            for k in range(l + 1, r):
                coins = dp(l, k) + dp(k, r) + a[l] * a[k] * a[r]
                total = max(total, coins)
            memo[(l, r)] = total
            return total

        return dp(0, len(nums) + 1)
