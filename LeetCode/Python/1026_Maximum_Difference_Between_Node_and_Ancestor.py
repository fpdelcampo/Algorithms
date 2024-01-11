    # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        def dfs(node, small, large):
            nonlocal res
            if node:
                small = min(small, node.val)
                large = max(large, node.val)
                res = max(res, abs(large-small))
                dfs(node.left, small, large)
                dfs(node.right, small, large)
        dfs(root, root.val, root.val)
        return res