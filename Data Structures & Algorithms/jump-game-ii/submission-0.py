class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums) # min jumps we need to get to index i
        dp[0] = 0 # starting position needs 0 jump 
        for i in range(1, len(nums)):
            for j in range(i):
                if (j + nums[j] >= i):
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
