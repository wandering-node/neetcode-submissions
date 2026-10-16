class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(i, curr):
            if i == len(s):
                ans.append(curr.copy())
                return
            for j in range(i, len(s)):
                sub = s[i : j + 1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    dfs(j + 1, curr)
                    curr.pop()
            return

        dfs(0, [])
        return ans
