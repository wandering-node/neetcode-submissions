class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            visited.add((r, c))
            directs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            for dr, dc in directs:
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < len(heights)
                    and 0 <= nc < len(heights[0])
                    and heights[nr][nc] >= heights[r][c]
                ):
                    dfs(nr, nc, visited)
            return

        for col in range(cols):
            dfs(0, col, pac)
            dfs(rows-1, col, atl)

        for row in range(rows):
            dfs(row, 0, pac)
            dfs(row, cols-1, atl)

        coords = []
        for coord in pac:
            if coord in atl:
                coords.append(list(coord))
        return coords
