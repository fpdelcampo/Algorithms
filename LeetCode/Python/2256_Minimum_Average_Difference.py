class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(nums[i] + pref[-1])
        suff = [0]
        for i in range(len(nums) - 1, -1, -1):
            suff.append(nums[i] + suff[-1])
        best = float('inf')
        idx = -1
        for i in range(len(nums)):
            start = floor(pref[i] / (i + 1))
            end = floor(suff[len(nums) - i - 1] / (len(nums) - i - 1)) if len(nums) - i - 1 != 0 else 0
            if abs(start - end) < best:
                best = abs(start - end)
                idx = i
        return idx