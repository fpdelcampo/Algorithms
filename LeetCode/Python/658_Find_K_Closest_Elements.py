class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x <= arr[0]:
            return arr[:k]
        n = len(arr)
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if arr[m] < x:
                l = m+1
            else:
                r = m-1
        l, r = r, l
        res = []
        while len(res) < k:
            if l >= 0 and r >= n:
                res.append(arr[l])
                l -= 1
            elif l < 0 and r < n:
                res.append(arr[r])
                r += 1
            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            print(res[-1])
        res.sort()
        return res