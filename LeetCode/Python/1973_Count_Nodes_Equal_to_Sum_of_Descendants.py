# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        res = 0
        def sum(root):
            nonlocal res
            if not root:
                return 0
            left = sum(root.left)
            right = sum(root.right)
            total = left + right + root.val
            if total == 2*root.val:
                res += 1
            return total
        sum(root)
        return res