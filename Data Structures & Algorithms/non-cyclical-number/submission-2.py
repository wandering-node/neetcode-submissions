class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def squared_sum(n):
            total = 0
            while n:
                n, digit = divmod(n, 10)
                total += digit**2
            return total
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = squared_sum(n)

        return True
        
        
