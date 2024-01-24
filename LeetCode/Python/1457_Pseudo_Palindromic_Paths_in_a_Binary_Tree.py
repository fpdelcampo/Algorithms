# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(node, path):
            nonlocal res
            if node:
                path[node.val - 1] += 1
                if not node.left and not node.right:
                    odd = False
                    pseudo = True
                    for i in range(9):
                        if path[i] % 2 == 1:
                            if odd:
                                pseudo = False
                            else:
                                odd = True
                    if pseudo:
                        res += 1
                dfs(node.left, [path[i] for i in range(9)])
                dfs(node.right, [path[i] for i in range(9)])
        path = [0 for _ in range(9)]
        dfs(root, path)
        return res