# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        q = deque()
        q.append(root)
        normal = True
        res = []
        while q:
            row = deque()
            iters = len(q)
            for _ in range(iters):
                node = None
                node = q.popleft()
                if normal:
                    row.append(node.val)
                else:
                    row.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(list(row))
            normal = not normal
        return res