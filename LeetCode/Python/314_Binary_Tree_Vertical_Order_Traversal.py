# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append([root, 0])
        vertical = {}
        while q:
            items = len(q)
            for i in range(items):
                node, alignment = q.popleft()
                if alignment not in vertical:
                    vertical[alignment] = [node.val]
                else:
                    vertical[alignment].append(node.val)

                if node.left:
                    q.append([node.left, alignment-1])
                if node.right:
                    q.append([node.right, alignment+1])
        vertical = dict(sorted(vertical.items()))
        res = []
        for key in vertical:
            res.append(vertical[key])
        return res