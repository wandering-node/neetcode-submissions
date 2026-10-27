class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        max_len = 0
        memo = {}
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, prev):
            if not (0 <= r < rows) or not (0 <= c < cols) or prev >= matrix[r][c]:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            tmp_len = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                tmp_len = max(tmp_len, dfs(nr, nc, matrix[r][c]))
            memo[(r, c)] = tmp_len + 1
            return memo[(r, c)]

        for r in range(rows):
            for c in range(cols):
                max_len = max(max_len, dfs(r, c, float("-inf")))
        return max_len
