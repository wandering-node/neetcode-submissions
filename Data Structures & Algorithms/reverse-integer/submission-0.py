class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        minN = -(2**31)
        maxN = 2**31 - 1
        is_pos = x > 0
        for i in range(len(str(abs(x)))-1, -1, -1):
            char = str(abs(x))[i]
            if res > maxN // 10 or res < int(minN / 10):
                return 0
            if res == maxN // 10 and int(char) > maxN % 10:
                return 0
            if res == int(minN / 10) and int(char) > (10 - minN % 10):
                return 0
            res *= 10
            if is_pos:
                res += int(char)
            else:
                res -= int(char)
        return res
