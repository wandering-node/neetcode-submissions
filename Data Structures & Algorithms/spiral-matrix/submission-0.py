class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        output = [] 
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                output.append(matrix[top][i])
            for i in range(top + 1, bottom + 1):
                output.append(matrix[i][right])
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    output.append(matrix[bottom][i])
            if left != right:
                for i in range(bottom - 1, top, -1):
                    output.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        return output
