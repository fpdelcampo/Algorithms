# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if not root:
            return 0
        graph = {}
        def dfs(node):
            nonlocal graph
            if node:
                if node.val not in graph:
                    graph[node.val] = []
                if node.left:
                    graph[node.left.val] = [node.val]
                    graph[node.val].append(node.left.val)
                if node.right:
                    graph[node.right.val] = [node.val]
                    graph[node.val].append(node.right.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        q = deque([start])
        visited = set([start])
        res = 0
        while q:
            iters = len(q)
            for _ in range(iters):
                next = q.popleft()
                nodes = graph[next]
                for node in nodes:
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
            res += 1
        return res-1