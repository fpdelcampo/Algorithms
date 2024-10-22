# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        q = deque([root])
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                s += node.val
            levels.append(s)
        levels.sort(reverse=True)
        return levels[k - 1] if k - 1 < len(levels) else -1