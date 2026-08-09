class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums:
                return [i, nums.index(rem)]