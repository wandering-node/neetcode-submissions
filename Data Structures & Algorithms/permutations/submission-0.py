class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        chosen = [False] * len(nums)
        curr = []
        res = []
        def dfs():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for i in range(len(nums)):
                if chosen[i]:
                    continue
                chosen[i] = True
                curr.append(nums[i])

                dfs()
                curr.pop()
                chosen[i] = False
        dfs()
        return res