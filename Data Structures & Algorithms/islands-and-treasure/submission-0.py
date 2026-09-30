class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        chests = collections.deque([])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    chests.append((row, col))

        step = 0
        while chests:
            step += 1
            for _ in range(len(chests)):
                r, c = chests.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == (2**31 - 1):
                        chests.append((nr, nc))
                        grid[nr][nc] = step
        return