# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        path = []
        def dfs(node):
            nonlocal path
            if node:
                dfs(node.left)
                path.append(node.val)
                dfs(node.right)
        dfs(root)
        return path[k-1]