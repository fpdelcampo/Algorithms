# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        tree = []
        def dfs(node):
            nonlocal tree
            if node:
                dfs(node.left)
                tree.append((abs(node.val - target), node.val))
                dfs(node.right)
        dfs(root)
        heapq.heapify(tree)
        res = []
        for _ in range(k):
            x, y = heapq.heappop(tree)
            res.append(y)
        return res