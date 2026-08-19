class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        
        l_row, r_row = 0, m
        l_col, r_col = 0, n

        while l_row <= r_row:
            mid_row = (l_row + r_row) // 2
            if target > matrix[mid_row][n]:
                l_row = mid_row + 1
            elif target < matrix[mid_row][0]:
                r_row = mid_row - 1
            else:
                target_row = matrix[mid_row]
                while l_col <= r_col:
                    mid_col = (l_col + r_col) // 2
                    if target > target_row[mid_col]:
                        l_col = mid_col + 1
                    elif target < target_row[mid_col]:
                        r_col = mid_col - 1
                    else:
                        return True
                return False
        return False
                
