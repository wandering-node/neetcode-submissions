class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(i, curr):
            if i == len(nums):
                ans.append(curr.copy())
                return
            # for j in range(i, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(0, [])
        return ans