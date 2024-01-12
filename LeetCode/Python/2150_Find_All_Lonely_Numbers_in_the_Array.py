class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        if len(nums) == 2:
            return nums if nums[0] != nums[1] and abs(nums[0] - nums[1]) != 1 else []
        tmp = sorted(list(set(nums)))
        c = Counter(nums)
        res = []
        for i in range(1, len(tmp)-1):
            if c[tmp[i]] == 1 and tmp[i-1] != tmp[i] - 1 and tmp[i+1] != tmp[i] + 1:
                res.append(tmp[i])
        if c[tmp[0]] == 1 and tmp[0] != tmp[1] - 1:
            res.append(tmp[0])
        if c[tmp[-1]] == 1 and tmp[-1] != tmp[-2] + 1:
            res.append(tmp[-1])
        return res