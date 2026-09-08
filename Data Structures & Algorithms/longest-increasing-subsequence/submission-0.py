class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dp = [0] * len(nums)
        dp[-1] = 1
        LIS = 1
        for i in range(len(nums) - 2, -1, -1):
            curr = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    curr = max(curr, dp[j] + 1)
            dp[i] = curr
            LIS = max(LIS, curr)
        return LIS
