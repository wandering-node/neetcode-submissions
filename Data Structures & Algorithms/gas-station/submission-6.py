class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = total = 0
        start = 0
        for i in range(len(gas)):
            supply = gas[i]
            demand = cost[i]
            tank += supply - demand
            if tank < 0:                
                tank = 0
                start = i + 1
            total += supply - demand
        return start if total >= 0 else -1