class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        selected = [False] * len(nums)

        def dfs(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            for idx, select in enumerate(selected):
                if not select:
                    curr.append(nums[idx])
                    selected[idx] = True
                    dfs(i + 1, curr)
                    curr.pop()
                    selected[idx] = False

        dfs(0, [])
        return res
