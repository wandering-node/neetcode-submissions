class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        limit = 2**31 - 1 if sign == 1 else 2**31
        x = abs(x)
        res = 0
        while x:
            x, digit = divmod(x, 10)
            if res > (limit - digit) // 10:
                return 0
            res = 10 * res + digit

        return sign * res
