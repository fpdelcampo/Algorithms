class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        # for each node, we perform a bfs.  store the nodes at distance M, end then for each of these distances, we create a return array
        distance = dict([(i, 0) for i in range(n)])
        x -= 1
        y -= 1
        def bfs(start):
            nonlocal x
            nonlocal y
            nonlocal distance
            q = deque([[start, -1]])
            visited = set([start])
            while q:
                length = len(q)
                for _ in range(length):
                    node, dist = q.popleft()
                    if dist != -1:                
                        distance[dist] += 1
                    if node == x and y not in visited:
                        visited.add(y)
                        q.append([y, dist + 1])
                    if node == y and x not in visited:
                        visited.add(x)
                        q.append([x, dist + 1])
                    if node < n - 1 and node + 1 not in visited:
                        visited.add(node + 1)
                        q.append([node + 1, dist + 1])
                    if node > 0 and node - 1 not in visited:
                        visited.add(node - 1)
                        q.append([node - 1, dist + 1])
        for i in range(n):
            bfs(i)
        res = [0 for _ in range(n)]
        for i in range(n):
            res[i] = distance[i]
        return res