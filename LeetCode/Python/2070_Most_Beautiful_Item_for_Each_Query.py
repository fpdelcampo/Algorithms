# We can probably divide the space of possible prices into segments that map to a particular maximum beauty
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items = sorted(items, key = lambda x: (x[0], -x[1]))
        monotonic = []
        curr = 0
        for item in items:
            price, beauty = item
            curr = max(curr, beauty)
            monotonic.append(curr)
        res = []
        for query in queries:
            pos = bisect_left(items, [query, float('inf')])
            
            if pos == len(items) or items[pos][0] > query:
                pos -= 1
            
            if pos >= 0:
                res.append(monotonic[pos])
            else:
                res.append(0)
        return res