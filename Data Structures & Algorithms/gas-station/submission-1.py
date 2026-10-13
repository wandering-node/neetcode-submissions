class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        while start < len(gas):
            tank = 0
            step = 0
            while step < len(gas):
                idx = (start + step) % len(gas)
                if (tank + gas[idx]) < cost[idx]:
                    break
                tank += gas[idx] - cost[idx]
                step += 1
            if step == len(gas):
                return start
            else:
                start += step + 1
        return -1


