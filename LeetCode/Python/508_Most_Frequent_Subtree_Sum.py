# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(lambda: 0)
        def sum(root):
            nonlocal freq
            if not root:
                return 0
            left = sum(root.left)
            right = sum(root.right)
            total = left + right + root.val
            freq[total] += 1
            return total
        sum(root)
        freq = dict(freq)
        m = -1
        for key in freq:
            m = max(m, freq[key])
        res = []
        for key in freq:
            if freq[key] == m:
                res.append(key)
        return res