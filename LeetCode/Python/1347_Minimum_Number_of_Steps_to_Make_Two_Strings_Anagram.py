class Solution:
    # Need to give them the same counts
    def minSteps(self, s: str, t: str) -> int:
        c1 = Counter(s)
        c2 = Counter(t)
        res = 0
        for key in c1:
            if key not in c2:
                res += c1[key]
            elif c1[key] > c2[key]:
                res += c1[key] - c2[key]
        return res