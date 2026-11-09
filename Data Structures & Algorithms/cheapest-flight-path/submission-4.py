class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        # tickets = {}
        # for u, v, cost in flights:
        #     if u in tickets:
        #         tickets[u].append((v, cost))
        #     else:
        #         tickets[u] = [(v, cost)]
        for _ in range(k + 1):
            new_costs = costs.copy()
            for u, v, cost in flights:
                new_costs[v] = min(costs[u] + cost, new_costs[v])
            costs = new_costs
        return new_costs[dst] if new_costs[dst] != float('inf') else -1
