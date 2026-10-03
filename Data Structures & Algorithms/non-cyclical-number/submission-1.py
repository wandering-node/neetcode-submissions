class Solution:
    def isHappy(self, n: int) -> bool:
        squared = {'0': 0, '1': 1, '2': 4, '3': 9, '4': 16, '5': 25, '6': 36, '7': 49, '8': 64, '9': 81}
        seen = set()
        prev = str(n)
        while prev not in seen:
            seen.add(prev)
            curr = 0
            for digit in prev:
                curr += squared[digit]
            if curr == 1:
                return True
            else:
                prev = str(curr)
                
        return False
