class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

        def dfs(r, c):
            if board[r][c] != "O":
                return
            board[r][c] = "*"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc)

        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "*":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
        return
