class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            curr = nums[i]
            rem = target - curr
            if rem in nums[i+1:]:
                return [i, nums[i+1:].index(rem)]