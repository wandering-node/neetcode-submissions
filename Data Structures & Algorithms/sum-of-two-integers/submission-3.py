class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        while b != 0:
            sum_no_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = sum_no_carry
            b = carry
        
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)