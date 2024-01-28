# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        mod = 1
        while q:
            n = len(q)
            high = -1
            low = 1000001
            for _ in range(n):
                node = q.popleft()
                if node.val % 2 != mod:
                    return False
                if mod and node.val <= high:
                    return False
                if not mod and node.val >= low:
                    return False
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                low = min(low, node.val)
                high = max(high, node.val)
            mod ^= 1
        return True