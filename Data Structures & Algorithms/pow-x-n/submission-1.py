class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {0: 1, 1: x}

        def halve(n):
            if n in memo:
                return memo[n]
            if n % 2:
                memo[n] = halve(n // 2) * halve(n // 2) * x
            else:
                memo[n] = halve(n // 2) * halve(n // 2)
            return memo[n]

        halve(abs(n))
        if n >= 0:
            return memo[n]
        else:
            return 1 / memo[abs(n)]
