# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or not p or not q:
            return False
        p_visit = []
        q_visit = []
        d = {}
        def p_dfs(root, target):
            if not root:
                return False
            d[root.val] = root
            if root == target:
                return True
            if p_dfs(root.left, target):
                p_visit.append(root.left.val)
                return True
            if p_dfs(root.right, target):
                p_visit.append(root.right.val)
                return True
            return False
        def q_dfs(root, target):
            if not root:
                return False
            d[root.val] = root
            if root == target:
                return True
            if q_dfs(root.left, target):
                q_visit.append(root.left.val)
                return True
            if q_dfs(root.right, target):
                q_visit.append(root.right.val)
                return True
            return False
        p_dfs(root, p)
        q_dfs(root, q)
        p_visit.append(root.val)
        q_visit.append(root.val)
        p_visit = p_visit[::-1]
        q_visit = q_visit[::-1]
        path = []
        m = min(len(p_visit), len(q_visit))
        i = 0
        while i < m:
            if p_visit[i] == q_visit[i]:
                path.append(p_visit[i])
            else:
                break
            i += 1
        return d[path[-1]]
 