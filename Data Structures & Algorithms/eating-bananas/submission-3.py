class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for i in range(len(piles)):
                time += math.ceil(piles[i] / mid)
            print(l, r, time)
            if time > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
