class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # square index is the key: row // 3 * 3 + col // 3
        mem = [[set() for _ in range(9)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    # if empty entry, no update, continue to the next one
                    continue
                curr = board[i][j]
                sqr_idx = (i // 3) * 3 + (j // 3)
                if curr in mem[0][i] or curr in mem[1][j] or curr in mem[2][sqr_idx]:
                    return False
                else:
                    mem[0][i].add(curr)
                    mem[1][j].add(curr)
                    mem[2][sqr_idx].add(curr)
        return True