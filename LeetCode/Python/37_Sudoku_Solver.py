class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[0 for j in range(9)] for i in range(9)]
        cols = [[0 for j in range(9)] for i in range(9)]
        boxes = [[0 for j in range(9)] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])-1
                    rows[i][num] = 1
                    cols[j][num] = 1
                    boxes[self.to_box(i, j)][num] = 1
        def solve(x, y):
            if x >= 9:
                return True
            if y == 9:
                return solve(x + 1, 0)
            if board[x][y] != '.':
                return solve(x, y + 1)
            for i in range(1, 10):
                box = self.to_box(x, y)
                num = i-1
                if not rows[x][num] and not cols[y][num] and not boxes[box][num]:
                    board[x][y] = str(i)
                    rows[x][num] = 1
                    cols[y][num] = 1
                    boxes[box][num] = 1
                    if solve(x, y+1):
                        return True
                    board[x][y] = '.'
                    rows[x][num] = 0
                    cols[y][num] = 0
                    boxes[box][num] = 0
        solve(0, 0)

    def to_box(self, x, y):
        return (x // 3) * 3 + (y // 3)
