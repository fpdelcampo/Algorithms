# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left) + 1
            right = dfs(root.right) + 1
            if root.left and root.left.val - 1 != root.val:
                left = 1
            if root.right and root.right.val - 1 != root.val:
                print(root.val, root.right.val)
                right = 1
            ans = max(ans, left, right)
            return max(left, right)
        dfs(root)
        return ans