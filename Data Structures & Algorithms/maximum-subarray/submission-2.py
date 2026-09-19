class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]
        for num in nums[1:]:
            if curr >= 0:
                curr += num
            else:
                curr = num
            res = max(res, curr)
        return res
                
        