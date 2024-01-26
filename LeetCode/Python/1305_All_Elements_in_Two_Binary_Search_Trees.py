# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        path1 = []
        path2 = []
        def dfs1(node):
            nonlocal path1
            if node:
                dfs1(node.left)
                path1.append(node.val)
                dfs1(node.right)
        def dfs2(node):
            nonlocal path2
            if node:
                dfs2(node.left)
                path2.append(node.val)
                dfs2(node.right)
        dfs1(root1)
        dfs2(root2)
        path1.extend(path2)
        path1.sort()
        return path1