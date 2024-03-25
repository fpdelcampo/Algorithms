class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        s = sum(nums)
        t = s / 2
        res = 0
        while s > t:
            num = heapq.heappop(heap)
            s += num / 2 # because num has been negated
            heapq.heappush(heap, num / 2)
            res += 1
        return res
