class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, curr):
            res.append(curr.copy())
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        dfs(0, [])
        return res