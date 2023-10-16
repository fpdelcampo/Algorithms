class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        l = [c[x] for x in c]
        adj = len(l)
        l.sort()
        ans = 0
        for i in range(len(l)):
            x = l[i]
            arr = [ele for ele in l]
            arr.pop(i)
            while x != 0 and x in arr:
                x -= 1
                ans += 1
            l[i] = x
        return ans