class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rem = target - nums[i]
            if (rem in nums) and (rem != nums[i]):
                return [i, nums.index(rem)]