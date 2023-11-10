class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            x, y = point
            dist.append([x, y, (x**2 + y**2)**.5])
        dist = list(sorted(dist, key = lambda x: x[2]))
        res = []
        for i in range(k):
            res.append([dist[i][0], dist[i][1]])
        return res