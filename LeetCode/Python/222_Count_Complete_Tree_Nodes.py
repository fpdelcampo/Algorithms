# We need to beat the obvious O(n) solution
# Somehow need to leverage the fact that the tree is complete
# There might be some binary search method because of the "order" of the final level (there's no "gaps", it just goes node, node, node, end, never node, node, null, node)
# You can find the "mids" somehow, by taking a path of left, rights... There is in fact probably a way to easily map left rights into binary
# Let's say the height of the tree is 4 (so theres 8 nodes in the lowest level).
# The leftmost node can map to 0 (left, left, left) -> 0, right most would be 1 (right, right, right)
# The first left/right corresponds to the first bit, the second corresponds to the second, etc.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        curr = root
        height = 0
        while curr:
            curr = curr.left
            height += 1
        l, r = 0, 2 ** (height - 1)
        while  l < r:
            m = (l + r) // 2
            curr = root
            for i in range(height - 2, -1, -1):
                if 2 ** i & m:
                    curr = curr.right
                else:
                    curr = curr.left
            if curr:
                l = m + 1
            else:
                r = m
        return 2 ** (height - 1) - 1 + l