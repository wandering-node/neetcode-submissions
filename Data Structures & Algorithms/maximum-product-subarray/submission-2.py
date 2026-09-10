class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_val = nums[0]
        local_max = nums[0]
        local_min = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cand1 = num * local_max
            cand2 = num * local_min
            local_max = max(num, cand1, cand2)
            local_min = min(num, cand1, cand2)
            max_val = max(local_max, max_val)
        return max_val