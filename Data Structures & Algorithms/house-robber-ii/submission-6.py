class Solution:
    def rob(self, nums: List[int]) -> int:
        def simple_rob(houses):
            if len(houses) == 0:
                return 0
            if len(houses) == 1:
                return houses[0]

            dp = [0] * (len(houses) + 1)
            dp[1] = houses[0]
            for i in range(2, len(houses) + 1):
                dp[i] = max(dp[i - 1], houses[i - 1] + dp[i - 2])
            return dp[-1]
        if len(nums) == 1:
            return nums[0]
        return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))
