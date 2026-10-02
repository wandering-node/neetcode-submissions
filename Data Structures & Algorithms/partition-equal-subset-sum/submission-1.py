class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        goal = total // 2
        dp = [False for _ in range(goal + 1)]
        dp[0] = True
        for num in nums:
            for s in range(goal, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        return dp[goal]