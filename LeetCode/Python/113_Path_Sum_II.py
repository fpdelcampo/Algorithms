# Fairly simple question, its just a bit hard to track the right variables

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, targetSum, s, path):
            nonlocal res
            if not node:
                return
            s += node.val
            path.append(node.val)
            if s == targetSum and not node.left and not node.right:
                res.append(path[:])
            dfs(node.left, targetSum, s, path)
            dfs(node.right, targetSum, s, path)
            path.pop()
        dfs(root, targetSum, 0, [])
        return res