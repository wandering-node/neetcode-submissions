class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        ans = 0
        for idx, (g, c) in enumerate(zip(gas, cost)):
            if tank + g - c < 0:
                tank = 0
                ans = idx + 1
            else:
                tank += g - c
            total += g - c
        return ans if total >= 0 else -1