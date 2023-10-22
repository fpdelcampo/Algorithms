class Solution:
    # Try to do a 2-coloring
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return True
        left = set()
        right = set()

        def bfs(i):
            q = deque()
            q.append(i)
            while q:
                idx = q.popleft()
                if i not in left and i not in right:
                    left.add(i)
                if idx in left:
                    for element in graph[idx]:
                        if element in left:
                            return False
                        if element not in right:
                            right.add(element)
                            q.append(element)
                
                if idx in right:
                    for element in graph[idx]:
                        if element in right:
                            return False
                        if element not in left:
                            left.add(element)
                            q.append(element)
            return True
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True