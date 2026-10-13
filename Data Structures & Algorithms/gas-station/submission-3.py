class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        total = 0
        start = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            diff = g - c
            total += diff
            tank += diff
            if tank < 0:
                tank = 0
                start = i + 1
        return start if total >=0 else -1

