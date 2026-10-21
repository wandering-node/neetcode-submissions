class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cost = [float("inf")] * n
        cost[src] = 0

        for _ in range(k + 1):
            temp = cost.copy()
            for u, v, price in flights:
                if cost[u] == float("inf"):
                    continue
                new_cost = cost[u] + price
                temp[v] = min(temp[v], new_cost)
            cost = temp
        if cost[dst] == float("inf"):
            return -1
        return cost[dst]
