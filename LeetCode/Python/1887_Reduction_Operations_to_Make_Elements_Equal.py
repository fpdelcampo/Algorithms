class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        c = Counter(nums)
        c = dict(sorted(c.items()))
        res = 0
        i = 0
        for key in c:
            if i != 0:
                res += i * c[key]
            i += 1
        return res