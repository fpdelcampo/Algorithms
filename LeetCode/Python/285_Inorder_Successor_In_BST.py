# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # If a node has a right child, the inorder successor is the left-most descendant of that child
    # Otherwise, we "go up" take the minimum of the following, handling "None" as needed:
    # 1. Take the last parent node of p
    # 2. Take the last parent node of p with a right child and take the left-most descendant of that child
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        res = p.right
        if res:
            while res.left:
                res = res.left
            return res
        curr = root
        traverse = None
        while curr != p:
            if p.val > curr.val:
                curr = curr.right
            else:
                if curr.right:
                    traverse = curr
                res = curr
                curr = curr.left
        if traverse:
            traverse = traverse.right
            while traverse.left:
                traverse = traverse.left
            if not res:
                return traverse
            if traverse.val < res.val:
                return traverse
            else:
                return res
        return res
        
"""
            6
          /    \
        2       8
       / \     / \
      0   4   7   9
         / \
        3   5

"""