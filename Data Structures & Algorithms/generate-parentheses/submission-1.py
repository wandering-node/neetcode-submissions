class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(o, c, curr):
            if o > n:
                return
            if o == c == n:
                res.append(curr)
                return
            if o > c:
                dfs(o, c + 1, curr + ")")
            dfs(o + 1, c, curr + "(")

        dfs(0, 0, "")
        return res
