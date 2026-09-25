class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = n & 1
            n >>= 1
            res |= bit
            res <<= 1
        return res >> 1