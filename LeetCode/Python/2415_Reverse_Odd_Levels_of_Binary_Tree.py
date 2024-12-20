# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        depth = 1
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node and node.left and node.right:
                    q.append(node.left)
                    q.append(node.right)
                level.append(node)
            if depth % 2 == 0:
                for i in range(len(level) // 2):
                    level[i].val, level[len(level) - i - 1].val = level[len(level) - i - 1].val, level[i].val
            depth +=1 
        return root