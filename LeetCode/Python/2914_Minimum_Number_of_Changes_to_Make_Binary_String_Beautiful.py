# Thinking either a greedy or DP approach.  
# DP would be something like DP[i] = DP[i - 2] + 1, which is obviously wrong
# How would we do greedy? I think the intuition is that we just need each pair starting from 0,1 2,3, etc to equal each other, so we just count the number of such pairs where they are not equal

class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        for i in range(len(s) // 2):
            if s[2 * i] != s[2 * i + 1]:
                res += 1
        return res
        