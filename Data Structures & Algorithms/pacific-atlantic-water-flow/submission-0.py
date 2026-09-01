class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, visited, preHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited:
                return
            if heights[r][c] >= preHeight:
                visited.add((r, c))
                directions = {(-1, 0), (1, 0), (0, 1), (0, -1)}
                for direc in directions:
                    nr, nc = r + direc[0], c + direc[1]
                    dfs(nr, nc, visited, heights[r][c])

        pac, atl = set(), set()
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows - 1][col])
        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols-1])
        ans = []
        for c in range(cols):
            for r in range(rows):
                if (r, c) in pac and (r, c) in atl:
                    ans.append([r, c])
        return ans

