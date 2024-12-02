class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        edges = [[i + 1] for i in range(n - 1)]
        answers = []
        for query in queries:
            u, v = query
            edges[u].append(v)
            q = deque([[0, 0]])
            done = False
            seen = set([0])
            while not done:
                for _ in range(len(q)):
                    node, dist = q.popleft()
                    if node == n - 1:
                        answers.append(dist)
                        done = True
                        break
                    for neighbor in edges[node]:
                        if neighbor not in seen:
                            seen.add(neighbor)
                            q.append([neighbor, dist + 1])
        return answers