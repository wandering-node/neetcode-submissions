class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for _ in range(k + 1):
            new_costs = costs.copy()
            for u, v, cost in flights:
                new_costs[v] = min(costs[u] + cost, new_costs[v])
            costs = new_costs
        return costs[dst] if costs[dst] != float("inf") else -1
