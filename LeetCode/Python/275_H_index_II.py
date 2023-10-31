class Solution:
    # Can also use binary search
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        n = len(citations)
        for i in range(n):
            if citations[n-i-1] > i:
                h = i+1
        return h