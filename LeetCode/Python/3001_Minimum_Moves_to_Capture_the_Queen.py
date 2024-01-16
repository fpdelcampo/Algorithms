class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        rook = 2
        bishop = 2
        if a == e:
            if a == c and (b < d < f or b > d > f):
                rook = 2
            else:
                rook = 1
        elif b == f:
            if b == d and (a < c < e or a > c > e):
                rook = 2
            else:
                rook = 1
        else:
            rook = 2
        if c + d == e + f:
            if a + b == c + d and ((d > b > f) or (d < b < f) or (c < a < e) or (c > a > e)):
                bishop = 2
            else:
                bishop = 1
        elif c - d == e - f:
            if a - b == c - d and ((d > b > f) or (d < b < f) or (c < a < e) or (c > a > e)):
                bishop = 2
            else:
                bishop = 1
        else:
            bishop = 2
        return min(rook, bishop)      