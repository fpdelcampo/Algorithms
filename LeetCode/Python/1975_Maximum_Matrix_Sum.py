# This should have a greedy solution
# If there's an even number of negatives, I think we can make the sum positive.  Otherwise, I think we make it so that the number with lowest absolute value is negated and everything else is positive

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s = 0
        n = 0
        smallest = 100001
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s += abs(matrix[i][j])
                n += (matrix[i][j] < 0)
                smallest = min(smallest, abs(matrix[i][j]))
        if n % 2 == 0:
            return s
        else:
            return s - 2 * smallest