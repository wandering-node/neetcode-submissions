class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            tmp = matrix[n - i - 1]
            matrix[n - i - 1] = matrix[i]
            matrix[i] = tmp
        for row in range(n):
            for col in range(row + 1, n):
                tmp = matrix[col][row]
                matrix[col][row] = matrix[row][col]
                matrix[row][col] = tmp
        return

