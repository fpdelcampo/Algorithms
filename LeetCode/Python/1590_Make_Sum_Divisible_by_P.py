class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        s = sum(nums)
        r = s % p
        if r == 0:
            return 0
        res = float('inf')
        curr = 0
        mod = {0: -1}
        for i in range(len(nums)):
            curr += nums[i]
            curr %= p
            if ((curr - r + p) % p) in mod:
                res = min(res, i - mod[(curr - r + p) % p])
            mod[curr] = i
        return res if res != float('inf') else -1