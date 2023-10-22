class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        first_row = False
        first_col = False

        for i in range(cols):
            if matrix[0][i] == 0:
                first_row = True
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col = True

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, cols):
            if matrix[0][i] == 0:
                for k in range(rows):
                    matrix[k][i] = 0
            
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for k in range(cols):
                    matrix[i][k] = 0

        for i in range(1, cols):
            if matrix[0][i] == 0:
                for k in range(rows):
                    matrix[k][i] = 0

        if first_row:
            for i in range(cols):
                matrix[0][i] = 0

        if first_col:
            for i in range(rows):
                matrix[i][0] = 0