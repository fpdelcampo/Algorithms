class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        for query in queries:
            ans = 0
            for pair in points:
                x, y = pair
                cx, cy, r = query
                if ((x-cx)**2 + (y-cy)**2)**0.5 <= r:
                    ans += 1
            res.append(ans)
        return res