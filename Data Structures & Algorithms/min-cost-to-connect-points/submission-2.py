class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minH = [(0, 0)]
        visited = set()
        total_cost = 0
        while len(visited) < len(points):
            cost, idx = heapq.heappop(minH)
            if idx in visited:
                continue
            visited.add(idx)
            total_cost += cost
            x1, y1 = points[idx]
            for i, (x2, y2) in enumerate(points):
                if i not in visited:
                    distance = abs(x1 - x2) + abs(y1 - y2)
                    heapq.heappush(minH, (distance, i))
        return total_cost