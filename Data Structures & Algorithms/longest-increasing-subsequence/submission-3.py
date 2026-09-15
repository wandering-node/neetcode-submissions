class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] longest increasing subsequence up to now
        dp = [1] * len(nums)
        dp[0] = 1
        LIS = 1

        for i in range(1, len(nums)):
            currLen = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    currLen = max(dp[j] + 1, currLen)
            dp[i] = currLen
            LIS = max(LIS, currLen)
        return LIS
                