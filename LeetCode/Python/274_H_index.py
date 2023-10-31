class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        h = 0
        n = len(citations)
        for i in range(n):
            if citations[n-i-1] > i:
                h = i+1
        return h