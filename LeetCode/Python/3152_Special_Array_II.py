class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        starts = []
        ends = []
        init = 0
        curr = 0
        last = nums[0] % 2
        for i in range(1, len(nums)):
            if nums[i] % 2 != last:
                curr += 1
                if i == len(nums) - 1:
                    starts.append(init)
                    ends.append(curr)
            else:
                if init != curr:
                    starts.append(init)
                    ends.append(curr)
                init, curr = i, i
            last = nums[i] % 2
        for query in queries:
            x, y = query
            if x == y:
                res.append(True)
            elif not starts:
                res.append(False)
            else:
                idx = bisect_left(starts, x)
                if idx >= len(starts) or starts[idx] != x:
                    idx -= 1
                if starts[idx] <= x <= y <= ends[idx]:
                    res.append(True)
                else:
                    res.append(False)
        return res
        