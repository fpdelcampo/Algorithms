# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        q = deque([root])
        last = None
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i == 0:
                    last = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return last.val