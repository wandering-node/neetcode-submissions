class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if grid[r][c] == 0:
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    area += dfs(nr, nc)
            return area

        ans = 0
        for row in range(rows):
            for col in range(cols):
                ans = max(dfs(row, col), ans)
        return ans
