# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = 101
        i = 0
        j = n-1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j):
                res = j
                j -= 1
            else:
                i += 1
        if res == 101:
            return -1
        return res