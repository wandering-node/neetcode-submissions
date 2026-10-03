class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        treasure = collections.deque([])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    treasure.append((r, c))
                    visited.add((r, c))
        while treasure:
            for _ in range(len(treasure)):
                r, c = treasure.popleft()
                distance = grid[r][c]
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr, nc) not in visited:
                        grid[nr][nc] = distance + 1
                        visited.add((nr, nc))
                        treasure.append((nr, nc))
        return
