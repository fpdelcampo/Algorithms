# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Note that the max path sum starting at a given node is equal has some clear recurrences
        # The max path sum including a node N is of the following form: max(m.val, maxPathSum(N.left), maxPathSum(N.right), maxPathSum(N.left)+N.val, maxPathSum(N.right)+N.val, maxPathSum(N.left)+N.val+maxPathSum(N.right))
        # Thus, there are 6 paths including a particular node to consider
        # We can use DP to store the values for the left and right subtrees
        # We want to do a postorder traversal since the value corresponding to N depends on the values corresponding to N.left and N.right
        # Also need to ensure that at least one node is in the path
        zero = False
        dp = {}
        best = -1001
        def dfs(node):
            nonlocal zero
            nonlocal best
            if node:
                if node.val == 0:
                    zero = True
                best = max(best, node.val)
                left = 0
                right = 0
                if node.left:
                    left = dfs(node.left)
                    dp[node.left] = left
                if node.right:
                    right = dfs(node.right)
                    dp[node.right] = right
                dp[node] = max(node.val, node.val+left, node.val+right)
                return dp[node]
            else:
                return 0
        res = -1001
        def solve(node):
            nonlocal res
            if node:
                if node.left and node.right:
                    res = max(res, node.val, dp[node.left]+node.val+dp[node.right])
                if node.left:
                    res = max(res, node.val, dp[node.left]+node.val)
                    solve(node.left)
                if node.right:
                    res = max(res, node.val, dp[node.right]+node.val)
                    solve(node.right)
                res = max(res, node.val)
                
            else:
                return
        
        dfs(root)
        solve(root)
        if not zero and res == 0:
            return best
        return res