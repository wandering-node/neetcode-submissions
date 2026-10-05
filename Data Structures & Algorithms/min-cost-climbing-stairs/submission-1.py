class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # minimum cost to get to index 1
        minCost = [float("inf")] * (len(cost) + 1)
        minCost[0] = 0
        minCost[1] = 0
        for i in range(2, len(minCost)):
            minCost[i] = min(minCost[i - 2] + cost[i - 2], minCost[i - 1] + cost[i - 1])
        return minCost[-1]
