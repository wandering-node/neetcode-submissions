from functools import cache


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        @cache
        def dfs(i, j):
            curr = matrix[i][j]
            extra_path = 0
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                if (
                    (0 <= nr < len(matrix))
                    and (0 <= nc < len(matrix[0]))
                    and (matrix[nr][nc] > curr)
                ):
                    extra_path = max(extra_path, dfs(nr, nc))
            return 1 + extra_path

        maxPath = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                maxPath = max(maxPath, dfs(r, c))
        return maxPath
