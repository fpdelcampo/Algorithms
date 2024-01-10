class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows*cols-1
        while l <= r:
            m = (l+r)//2
            i, j = self.oneD_to_twoD(rows, cols, m)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = m+1
            else:
                r = m-1
        return False
    def oneD_to_twoD(self, m, n, x):
        i = x // n
        j = x % n
        return i, j


   