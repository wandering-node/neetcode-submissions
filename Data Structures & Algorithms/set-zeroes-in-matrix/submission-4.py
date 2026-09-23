class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_col_zero = False
        for i in range(len(matrix)): 
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range(len(matrix[0])): 
            if matrix[0][i] == 0:
                matrix[0][0] = 0
                break
            
        for i in range(1, len(matrix)): 
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for col in range(1, len(matrix[0])): 
            if matrix[0][col] == 0:
                for row in range(1, len(matrix)):
                    matrix[row][col] = 0
        
        for row in range(1, len(matrix)):
            if matrix[row][0] == 0:
                for col in range(1, len(matrix[0])):
                    matrix[row][col] = 0
        if matrix[0][0] == 0:
            for col in range(1, len(matrix[0])):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0