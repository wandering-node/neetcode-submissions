class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            half, carry = n // 2, n % 2
            ans = pow(x, half)
            if not carry:
                return ans * ans
            else:
                return ans * ans * x
        tmp = pow(x, abs(n))
        return tmp if n >= 0 else 1/tmp
