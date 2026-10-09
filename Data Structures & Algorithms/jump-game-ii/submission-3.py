class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        step = 0
        while r < len(nums) - 1:
            outbound = r + 1
            for i in range(l, outbound):
                r = max(r, i + nums[i])
            l = outbound
            step += 1
        return step