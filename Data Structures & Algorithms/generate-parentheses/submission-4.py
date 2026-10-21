class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dfs(l, r, curr):
            if l == r == n:
                ans.append(curr)
                return
            if l > n:
                return
            if l > r:
                dfs(l, r + 1, curr + ")")
                dfs(l + 1, r, curr + "(")
            elif l == r:
                dfs(l+1, r, curr + "(")
        dfs(0, 0, '')
        return ans