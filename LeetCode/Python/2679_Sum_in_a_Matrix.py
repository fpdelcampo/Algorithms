class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 4:
            return 0
        low_1 = float('inf')
        low_2 = float('inf')
        low_3 = float('inf')
        low_4 = float('inf')
        high_1 = float('-inf')
        high_2 = float('-inf')
        high_3 = float('-inf')
        high_4 = float('-inf')
        for num in nums:
            if num <= low_1:
                low_4 = low_3
                low_3 = low_2
                low_2 = low_1
                low_1 = num
            elif num <= low_2:
                low_4 = low_3
                low_3 = low_2
                low_2 = num
            elif num <= low_3:
                low_4 = low_3
                low_3 = num
            elif num <= low_4:
                low_4 = num

            if num >= high_1:
                high_4 = high_3
                high_3 = high_2
                high_2 = high_1
                high_1 = num
            elif num >= high_2:
                high_4 = high_3
                high_3 = high_2
                high_2 = num
            elif num >= high_3:
                high_4 = high_3
                high_3 = num
            elif num >= high_4:
                high_4 = num
        res = []
        if high_4 - low_1 > 0:
            res.append(high_4 - low_1)
        if high_3 - low_2 > 0:
            res.append(high_3 - low_2)
        if high_2 - low_3 > 0:
            res.append(high_2 - low_3)
        if high_1 - low_4 > 0:
            res.append(high_1 - low_4)
        if res:
            return min(res)
        return 0