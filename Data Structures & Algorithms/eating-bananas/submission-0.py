class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
        lb = 1
        ub = max(piles)
        while lb <= ub:
            time = 0
            mid = (lb + ub) // 2
            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                lb = mid + 1
            else:
                ub = mid - 1
        return lb
        