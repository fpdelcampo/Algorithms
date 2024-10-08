class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        freq = [0] * (mx + 1)
        for num in nums:
            freq[num] += 1

        gcds = [0] * (mx + 1)
        for i in range(mx, 0, -1):
            curr = 0
            for j in range(i, mx + 1, i):
                curr += freq[j]
            gcds[i] = curr * (curr - 1) // 2  # Combinatorial count
            for j in range(2 * i, mx + 1, i):
                gcds[i] -= gcds[j]
        prefix = []
        total = 0
        for i in range(1, mx + 1):
            total += gcds[i]
            prefix.append(total)
        res = []
        # print(prefix, gcds)
        for query in queries:
            idx = bisect_left(prefix, query + 1)
            res.append(idx + 1)
        return res