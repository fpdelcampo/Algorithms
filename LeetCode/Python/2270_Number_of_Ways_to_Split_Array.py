class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for i in range(1, len(nums)):
            pref.append(pref[-1] + nums[i])
        suff = [nums[-1] for  i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            suff[i] = suff[i + 1] + nums[i]
        res = 0
        for i in range(len(nums) - 1):
            if pref[i] >= suff[i + 1]:
                res += 1
        return res