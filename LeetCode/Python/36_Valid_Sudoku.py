class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = [set() for _ in range(9)]
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if (board[i][j] != '.' and board[i][j] in row) or (board[j][i] != '.' and board[j][i] in col):
                    return False
                box = self.to_box(i, j)
                if board[i][j] != '.' and board[i][j] in boxes[box]:
                    return False
                row.add(board[i][j])
                col.add(board[j][i])
                boxes[box].add(board[i][j])
        return True
    def to_box(self, x, y):
        if y < 3:
            if x < 3:
                return 0
            elif x < 6:
                return 1
            else:
                return 2
        elif y < 6:
            if x < 3:
                return 3
            elif x < 6:
                return 4
            else:
                return 5
        else:
            if x < 3:
                return 6
            elif x < 6:
                return 7
            else:
                return 8