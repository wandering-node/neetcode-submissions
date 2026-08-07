class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            curr = nums[i]
            rem = target - curr
            if rem in seen:
                return [seen[rem], i]
            else:
                seen[curr] = i