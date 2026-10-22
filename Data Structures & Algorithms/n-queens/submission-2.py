class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        ans = []
        # rows = set()
        cols = set()
        diag1 = set()
        diag2 = set()

        def placeQueens(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r + c)
                diag2.add(r - c)
                placeQueens(r + 1)
                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r + c)
                diag2.remove(r - c)

        placeQueens(0)
        return ans
