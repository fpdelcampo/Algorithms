class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        edges = {}
        for idx, route in enumerate(routes):
            for stop in route:
                if stop not in edges:
                    edges[stop] = [idx]
                else:
                    edges[stop].append(idx)
        q = deque()
        visited = set()
        for route in edges[source]:
            q.append(route)
            visited.add(route)
        layer = 1
        while q:
            iters = len(q)
            for _ in range(iters):
                route = q.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return layer
                    for next in edges[stop]:
                        if next not in visited:
                            visited.add(next)
                            q.append(next)
            layer += 1
        return -1