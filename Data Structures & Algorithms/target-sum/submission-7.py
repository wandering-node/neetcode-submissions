class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        visited = {}

        def dfs(i, curr):
            if (i, curr) in visited:
                return visited[(i, curr)]
            if i == len(nums) and curr == target:
                return 1
            if i >= len(nums):
                return 0
            

            addition = dfs(i + 1, curr + nums[i])
            subtraction = dfs(i + 1, curr - nums[i])
            visited[(i, curr)] = addition + subtraction
            return visited[(i, curr)]

        return dfs(0, 0)
