class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        c = dict(sorted(c.items(), key=lambda x: x[1]))
        ans = len(set(arr))
        for key in c:
            if c[key] > k:
                return ans
            else:
                ans -= 1
                k -= c[key]
        return ans