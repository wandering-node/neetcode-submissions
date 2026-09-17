class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # set the initial goal to be the last index
        goal = len(nums) - 1
        i = goal - 1
        while 0 <= i < goal:
            if nums[i] >= goal - i:
                goal = i
                i = goal - 1
            else:
                i -= 1
        return goal == 0