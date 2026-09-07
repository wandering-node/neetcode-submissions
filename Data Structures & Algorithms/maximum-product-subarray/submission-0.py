class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minim, maxim, global_max = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            cand1 = nums[i] * minim
            cand2 = nums[i] * maxim
            minim = min(nums[i], cand1, cand2)
            maxim = max(nums[i], cand1, cand2)
            global_max = max(maxim, global_max)
        return global_max
