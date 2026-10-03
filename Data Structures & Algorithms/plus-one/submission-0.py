class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        carry = 1
        for idx in range(len(digits) - 1, -1, -1):
            digit = digits[idx]
            carry, digit = divmod(digit + carry, 10)
            new_digits.append(digit)
        if carry:
            new_digits.append(carry)
        new_digits.reverse()        
        return new_digits
