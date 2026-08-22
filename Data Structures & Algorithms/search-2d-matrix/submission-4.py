class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            if matrix[row][-1] < target:
                continue
            else:
                l = 0
                r = n - 1
                while l <= r:
                    mid = (l+r)//2
                    if matrix[row][mid] == target:
                        return True
                    elif matrix[row][mid] > target:
                        r = mid -1
                    else:
                        l = mid + 1
        return False