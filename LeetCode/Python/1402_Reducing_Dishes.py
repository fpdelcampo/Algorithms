class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # satisfaction.sort()
        # res = 0
        # for i in range(len(satisfaction)):
        #     total = 0
        #     for j in range(i, len(satisfaction)):
        #         total += (j - i + 1) * satisfaction[j]
        #     res = max(res, total)
        # return res

        # Note: Originally I came up with sorting and then simply scanning the whole subarray.  This would give us 500*500/2 = 125000 operations.  On this problem, this approach passes, but it won't always presumably.  Therefore we can look to a more clever way.  We can take a suffix, update the suffix, and add the suffix to a cumulative satisfaction score.  This way, every time we at suffix to the cumulative score, we are affectively increasing the multiple of previously included satisfactions.  This reduces the scan to linear.

        satisfaction.sort()
        res = 0
        suffix = 0
        m = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            suffix += satisfaction[i]
            m += suffix
            res = max(res, m)
        return res