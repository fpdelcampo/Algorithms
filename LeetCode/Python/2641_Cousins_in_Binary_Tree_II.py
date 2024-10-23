# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea, first find level sums.
# Then do BFS. For each node, if

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        levels = []
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
        q = deque([root])
        i = 0
        root.val = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.left and node.right:
                    new = levels[i + 1] - node.left.val - node.right.val
                    node.left.val = new
                    node.right.val = new
                elif node.left:
                    node.left.val = levels[i + 1] - node.left.val
                elif node.right:
                    node.right.val = levels[i + 1] - node.right.val 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            i += 1
        return root