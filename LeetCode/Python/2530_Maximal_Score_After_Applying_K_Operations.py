class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        score = 0
        for _ in range(k):
            best = heapq.heappop(heap)
            heapq.heappush(heap, floor(best / 3))
            score -= best
        return score