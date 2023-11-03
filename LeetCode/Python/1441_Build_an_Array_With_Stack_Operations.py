class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        idx = 0
        res = []
        for i in range(1, n+1):
            if idx >= len(target):
                break
            if i == target[idx]:
                res.append('Push')
                idx += 1
            else:
                res.append('Push')
                res.append('Pop')
        return res