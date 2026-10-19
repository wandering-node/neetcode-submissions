class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(i, curr):
            if i == len(s):
                ans.append(curr.copy())
            for j in range(i, len(s)):
                sub = s[i: j+1]
                if sub == sub[::-1]:
                    curr.append(sub)
                    backtrack(j+1, curr)
                    curr.pop()
                
        backtrack(0, [])
        return ans