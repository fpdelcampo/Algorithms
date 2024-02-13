class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        low = min(nums)
        high = max(nums)
        idx1 = -1
        idx2 = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == low:
                idx1 = i
            if nums[i] == high:
                idx2 = i
        return min(1 + max(idx1, idx2), max(n - idx1, n - idx2), idx1 + 1 + n - idx2, idx2 + 1 + n - idx1)