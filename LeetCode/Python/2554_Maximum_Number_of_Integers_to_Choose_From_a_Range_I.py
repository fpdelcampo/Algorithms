class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        res, s = 0, 0
        for i in range(1, n + 1):
            if i not in banned:
                if s + i <= maxSum:
                    s += i
                    res += 1
                else:
                    return res
        return res