class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i in range(len(nums)):
            num = nums[i]
            rem = target - num
            if rem in mem:
                return [mem[rem], i]
            else:
                mem[num] = i
