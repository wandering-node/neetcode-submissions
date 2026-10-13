class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(l, r, curr):
            if l > n:
                return
            if l == r == n:
                res.append(curr)
                return
            if l > r:
                dfs(l, r + 1, curr + ")")
            dfs(l + 1, r, curr + "(")

        dfs(0, 0, "")
        return res
