class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, curr, curr_target):
            if curr_target == target:
                res.append(curr.copy())
                return
            if curr_target > target or idx >= len(nums):
                return
            curr.append(nums[idx])
            dfs(idx, curr, curr_target + nums[idx])
            curr.pop()
            dfs(idx + 1, curr, curr_target)
        dfs(0, [], 0)
        return res