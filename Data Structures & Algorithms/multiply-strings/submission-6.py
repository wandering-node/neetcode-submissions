class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        ans = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                n1, n2 = int(num1[i]), int(num2[j])
                carry, digit = divmod(ans[i + j + 1] + n1 * n2, 10)
                ans[i + j + 1] = digit
                ans[i + j] += carry
        return "".join([str(item) for item in ans]).lstrip("0")
