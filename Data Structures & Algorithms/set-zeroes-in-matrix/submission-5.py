class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        isZeroCol = False
        for i in range(rows):
            if matrix[i][0] == 0:
                    isZeroCol = True
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(1, cols):
                    matrix[i][j] = 0
                
        for i in range(1, cols):
            if matrix[0][i] == 0:
                for j in range(1, rows):
                    matrix[j][i] = 0

        if matrix[0][0] == 0:
            for col in range(1, len(matrix[0])):
                matrix[0][col] = 0
        if isZeroCol:
            for row in range(len(matrix)):
                matrix[row][0] = 0