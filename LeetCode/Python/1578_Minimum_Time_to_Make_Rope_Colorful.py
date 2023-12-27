class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        n = len(colors)
        i = 1
        while i < n:
            s = 0
            m = 0
            j = i-1
            while i < n and colors[i] == colors[i-1]:
                s += neededTime[i]
                m = max(m, neededTime[i])
                i += 1
            s += neededTime[j]
            m = max(m, neededTime[j])
            total += s - m
            i += 1
        return total