class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            t = 0
            for fruit in piles:
                t += math.ceil(fruit / mid)
            if t > h:
                l = mid + 1
            else:
                r = mid
        return l