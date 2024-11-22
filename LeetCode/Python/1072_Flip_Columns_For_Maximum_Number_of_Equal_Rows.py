class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        freq = defaultdict(lambda: 0)
        for row in matrix:
            pattern = ''.join(['T' if row[0] == entry else 'F' for entry in row])
            freq[pattern] += 1
        return max(freq.values())
        