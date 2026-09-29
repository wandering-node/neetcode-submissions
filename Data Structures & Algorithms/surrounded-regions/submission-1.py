class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if board[r][c] in ("X", "*"):
                return
            board[r][c] = "*"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)
            return

        for col in range(cols):
            dfs(0, col)
            dfs(rows - 1, col)
        for row in range(1, rows - 1):
            dfs(row, 0)
            dfs(row, cols - 1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "*":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return
