from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dfs(i, j):

            # Base case: pattern is exhausted
            if j == len(p):
                return i == len(s)

            # Does the current character match?
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            # Case 1: Next pattern character is '*'
            if j < len(p) - 1 and p[j + 1] == "*":

                # Option A: Skip the entire x* pattern
                skip = dfs(i, j + 2)

                # Option B: Match one character and
                # stay on x* to allow more repetitions
                repeat = first_match and dfs(i + 1, j)

                return skip or repeat

            # Case 2: No '*', match normally
            return first_match and dfs(i + 1, j + 1)

        return dfs(0, 0)
