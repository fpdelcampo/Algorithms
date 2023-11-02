# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def average(root):
            nonlocal res
            if not root:
                return 0, 0
            left_sum, left_num = average(root.left)
            right_sum, right_num = average(root.right)
            sum = left_sum + right_sum + root.val
            num = left_num + right_num + 1
            if sum//num == root.val:
                res += 1
            return sum, num
        average(root)
        return res