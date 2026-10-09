class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        goal, remainder = divmod(total, 2)
        if remainder:
            return False
        dp = [False] * (goal + 1)
        dp[0] = True  # dp[i] means if i can be achieved using number in nums
        for num in nums:
            for i in range(goal, num - 1, -1):
                dp[i] = dp[i] | dp[i - num]
        return dp[goal]
