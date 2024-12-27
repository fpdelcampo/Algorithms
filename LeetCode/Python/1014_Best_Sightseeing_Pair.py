class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        adj = [values[i] - i for i in range(len(values))]
        suffix = [0 for _ in range(len(values))]
        suffix[-1] = adj[-1]
        for i in range(len(values) - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], adj[i])
        res = -1
        for i in range(len(values) - 1):
            # print(i, values[i], suffix[i + 1])
            res = max(res, values[i] + i + suffix[i + 1])
        return res
