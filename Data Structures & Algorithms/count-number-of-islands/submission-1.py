class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if grid[r][c] == "0":
                return
            grid[r][c] = "0"
            directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= (rows - 1) and 0 <= nc <= (cols - 1):
                    dfs(nr, nc)
            return

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(row, col)
        return islands
