class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        q = []
        heapq.heapify(q)
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff > 0:
                heapq.heappush(q, diff)
                if len(q) > ladders:
                    bricks -= heapq.heappop(q)
                    if bricks < 0:
                        return i - 1
        return len(heights) - 1