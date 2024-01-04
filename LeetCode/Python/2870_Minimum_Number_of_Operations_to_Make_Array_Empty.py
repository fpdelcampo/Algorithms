class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = dict(Counter(nums))
        s = 0
        for key in c:
            if c[key] == 1:
                return -1
            if c[key] % 3 == 0:
                s += c[key] // 3
            if c[key] % 3 == 1:
                s += 2 + (c[key]-4)//3
            if c[key] % 3 == 2:
                s += 1 + (c[key]-2)//3
        return s