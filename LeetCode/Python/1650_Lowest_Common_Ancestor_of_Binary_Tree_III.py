"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        dictionary = {}
        p_path = []
        c1 = p
        prev = None
        while c1:
            dictionary[c1.val] = c1
            p_path.append(c1.val)
            prev = c1
            c1 = c1.parent
        q_path = []
        c2 = q
        while c2:
            dictionary[c2.val] = c2
            q_path.append(c2.val)
            c2 = c2.parent
        p_path = p_path[::-1]
        q_path = q_path[::-1]
        path = []
        i = 0
        prev
        while i < min(len(p_path), len(q_path)):
            if p_path[i] != q_path[i]:
                break
            else:
                path.append(p_path[i])
            i += 1
        return dictionary[path[-1]]
