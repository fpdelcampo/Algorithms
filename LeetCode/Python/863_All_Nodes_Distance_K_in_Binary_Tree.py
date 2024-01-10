# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return 0
        if k == 0:
            return [target.val]
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
        q = deque([target.val])
        visited = set([target.val])
        height = 0
        res = []
        while q:
            iters = len(q)
            for _ in range(iters):
                next = q.popleft()
                nodes = graph[next]
                for node in nodes:
                    if node not in visited:
                        q.append(node)
                        visited.add(node)
                        if height == k-1:
                            res.append(node)
            if res:
                return res
            height += 1
        return res