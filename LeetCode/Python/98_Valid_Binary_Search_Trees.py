# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Attempt 1
        # Time: O(n), Space: O(n)
        if not root:
            return True
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        init = res[0]
        for num in res[1:]:
            if num <= init:
                return False
            init = max(num, init)
        return True