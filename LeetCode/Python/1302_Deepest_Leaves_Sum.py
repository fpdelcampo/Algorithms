# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        s = 0
        q = deque()
        q.append(root)
        while q:
            iters = len(q)
            row = 0
            for _ in range(iters):
                node = q.popleft()
                row += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            s = row
        return s