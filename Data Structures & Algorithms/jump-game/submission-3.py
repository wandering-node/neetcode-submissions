class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = 0
        for i in range(len(nums)):
            if curr < i:
                return False
            curr = max(i + nums[i], curr)
        return curr >= (len(nums) - 1)
