class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        squares = [] # a list of points that are attacked by a queen
        res = []
        def backtrack(row, y, d, ad, sequence, n):
            nonlocal res
            if len(sequence) == n:
                res.append(self.seq2str(sequence, n))
                return
            for col in range(n):
                if (col in y or (row+col) in d or (row-col) in ad):
                    continue
                else:
                    y.append(col)
                    d.append(row+col)
                    ad.append(row-col)
                    sequence.append((row, col))
                    backtrack(row+1, y, d, ad, sequence, n)
                    y.pop()
                    d.pop()
                    ad.pop()
                    sequence.pop()
        backtrack(0, [], [], [], [], n)
        return res
    
    def seq2str(self, seq, n):
        board1 = [["." for _ in range(n)] for _ in range(n)]
        board2 = []
        for point in seq:
            x, y = point
            board1[x][y] = "Q"
            board2.append(''.join(board1[x]))
        return board2