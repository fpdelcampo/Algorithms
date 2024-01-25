class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        c = dict(sorted(c.items(), key = lambda x: x[1], reverse = True))
        n = len(arr)
        res = 0
        for key in c:
            n -= c[key]
            res += 1
            if n <= len(arr) // 2:
                return res
        return res