class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            if r < 0 or r >= rows or c < 0 or c >= cols:
                memo[(r, c)] = 0
                return memo[(r, c)]

            max_step = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_step = max(max_step, 1 + dfs(nr, nc))
            memo[(r, c)] = max_step
            return memo[(r, c)]

        maxPath = 0
        for i in range(rows):
            for j in range(cols):
                currPath = dfs(i, j)
                maxPath = max(maxPath, currPath)
        return maxPath
