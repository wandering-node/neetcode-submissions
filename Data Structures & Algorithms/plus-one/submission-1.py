class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        res = []
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i]
            num, carry = (digit + carry) % 10, (digit + carry) // 10
            res.append(num)
        if carry:
            res.append(carry)
        res.reverse()
        return res