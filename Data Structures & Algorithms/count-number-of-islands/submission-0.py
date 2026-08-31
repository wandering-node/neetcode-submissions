class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            queue = collections.deque()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr <= rows - 1
                        and 0 <= nc <= cols - 1
                        and grid[nr][nc] == "1"
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands
