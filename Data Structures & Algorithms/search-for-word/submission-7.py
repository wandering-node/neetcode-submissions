class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        def dfs(row, col, idx):
            direcs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if idx >= len(word):
                return True
            for r, c in direcs:
                new_r, new_c = row + r, col + c
                if (new_r >= rows) or (new_c >= cols) or (new_r < 0) or (new_c < 0) or ((new_r, new_c) in visited) or (board[new_r][new_c] != word[idx]):
                    continue
                if board[new_r][new_c] == word[idx]:
                    visited.add((new_r, new_c))
                    if dfs(new_r, new_c, idx + 1):
                        return True
                    visited.remove((new_r, new_c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set([(r, c)])
                    if dfs(r, c, 1):
                        return True
        return False

        


