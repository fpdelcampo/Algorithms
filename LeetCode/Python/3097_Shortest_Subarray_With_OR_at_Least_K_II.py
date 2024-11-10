class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        bits = 32 * [0]
        start = 0
        end = 0
        minimum = float('inf')
        def conv(bits):
            res = 0
            for i in range(32):
                if bits[i] != 0:
                    res |= (1 << i)
            return res
        while end < len(nums):
            for i in range(32):
                if (1 << i) & nums[end]:
                    bits[i] += 1
            while start <= end and conv(bits) >= k:
                minimum = min(minimum, end - start + 1)
                for i in range(32):
                    if (1 << i) & nums[start] and bits[i] > 0:
                        bits[i] -= 1
                start += 1
            end += 1
        return -1 if minimum == float('inf') else minimum