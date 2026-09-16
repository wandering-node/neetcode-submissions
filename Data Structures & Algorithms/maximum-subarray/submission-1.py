class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr >= 0:
                curr += nums[i]
            else:
                curr = nums[i]
            result = max(curr, result)
        return result