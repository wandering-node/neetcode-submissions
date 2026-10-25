class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1, digit2 = int(num1[i]), int(num2[j])
                product = digit1 * digit2
                pos1, pos2 = i + j, i + j + 1
                total = product + res[pos2]
                carry, digit = divmod(total, 10)
                res[pos1] += carry
                res[pos2] = digit
        res = [f"{d}" for d in res]
        return "".join(res).lstrip("0")