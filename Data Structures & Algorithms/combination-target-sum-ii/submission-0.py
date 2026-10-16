class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(i, curr, curr_tar):
            if curr_tar == target:
                ans.append(curr.copy())
                return
            if i == len(candidates) or curr_tar > target:
                return
            curr.append(candidates[i])
            dfs(i + 1, curr, curr_tar + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, curr_tar)
            return

        dfs(0, [], 0)
        return ans
