class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first row is for row validity, second for column, third for square
        valid_sets = [[set() for _ in range(9)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                if (curr := board[row][col]) == ".":
                    # if empty entry, no update, continue to the next one
                    continue

                # extract corresponding test sets
                row_set = valid_sets[0][row]
                col_set = valid_sets[1][col]
                square_set = valid_sets[2][3 * (row // 3) + (col // 3)]
                if (curr in row_set) or (curr in col_set) or (curr in square_set):
                    return False
                else:
                    row_set.add(curr)
                    col_set.add(curr)
                    square_set.add(curr)

        return True
