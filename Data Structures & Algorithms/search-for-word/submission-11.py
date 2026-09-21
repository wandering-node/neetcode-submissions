class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        def dfs(r, c, idx):
            if idx == len(word) - 1 and board[r][c] == word[idx]:
                return True
            if board[r][c] == word[idx]:
                visited.add((r, c))
                for dr, dc in directions:
                    newr, newc = r + dr, c + dc
                    if 0 <= newr < rows and 0 <= newc < cols and (newr, newc) not in visited:
                        if dfs(newr, newc, idx + 1):
                            return True
                visited.remove((r, c))
            return False
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False

