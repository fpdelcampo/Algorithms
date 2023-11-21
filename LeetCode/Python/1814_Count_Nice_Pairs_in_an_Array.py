class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        diff = {}
        res = 0
        for num in nums:
            if num-int(str(num)[::-1]) in diff:
                diff[num-int(str(num)[::-1])] += 1
            else:
                diff[num-int(str(num)[::-1])] = 1
        for key in diff:
            res += diff[key]*(diff[key]-1)//2
        return res % (10**9 + 7)