class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            if curr >= 0 and (curr + nums[i]) >= 0:
                curr += nums[i]
                # print(f'step {i}, add {nums[i]} to curr')
            else:
                curr = nums[i]
                # print(f'step {i}, update curr to {nums[i]} ')
            result = max(curr, result)
            # print(f'step {i}, result is {result} ')
        return result