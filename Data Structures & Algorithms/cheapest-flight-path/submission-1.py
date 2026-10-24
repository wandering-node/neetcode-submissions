class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")] * n
        cost[src] = 0

        for _ in range(k+1):
            tmp = cost.copy()
            for s, d, c in flights:
                # if cost[s] == float('inf'):
                #     continue
                
                tmp[d] = min(tmp[d], cost[s] + c)
            cost = tmp
        return cost[dst] if cost[dst] != float("inf") else -1
        
        
       