from math import factorial


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        choice1 = m - 1
        choice2 = n - 1
        return int(factorial(total) / factorial(choice1) / factorial(choice2))
