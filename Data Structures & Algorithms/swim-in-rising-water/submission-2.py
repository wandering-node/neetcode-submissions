class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        minH = [(grid[0][0], 0, 0)]
        visited = set()
        time = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while minH:
            t, r, c = heapq.heappop(minH)
            visited.add((r, c))
            time = max(time, t)
            if r == c == n - 1:
                return time
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and 0 <= nr <= n - 1 and 0 <= nc <= n - 1:
                    heapq.heappush(minH, (grid[nr][nc], nr, nc))
