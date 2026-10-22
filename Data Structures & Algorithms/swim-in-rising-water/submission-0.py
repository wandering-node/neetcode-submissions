class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        minH = [(grid[0][0], 0, 0)]
        visited = set((0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minH:
            time, r, c = heapq.heappop(minH)

            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= n or nc < 0 or nc >= n or (nr, nc) in visited:
                    continue
                visited.add((nr, nc))
                newTime = max(time, grid[nr][nc])
                heapq.heappush(minH, (newTime, nr, nc))
