"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return None
        q = deque([root])
        res = []
        while q:
            row = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                row.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(row)
        return res
