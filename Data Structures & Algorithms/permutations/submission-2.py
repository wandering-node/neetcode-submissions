class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        selected = [False] * len(nums)
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for idx, select in enumerate(selected):
                if not select:
                    curr.append(nums[idx])
                    selected[idx] = True
                    dfs()
                    curr.pop()
                    selected[idx] = False
        dfs()
        return res
                