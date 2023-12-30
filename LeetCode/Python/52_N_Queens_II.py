class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        def backtrack(row, y, d, ad, sequence, n):
            nonlocal res
            if len(sequence) == n:
                res += 1
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