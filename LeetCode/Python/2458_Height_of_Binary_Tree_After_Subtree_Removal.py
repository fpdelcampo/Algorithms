# Observations: We probably need to do this in linear time
# General approach: We should probably first compute the "subtree depth", ie the depth of the subtree whose root is a particular node
# In addition, we should probably have a map children_to_parent that maps a node to its parent. Then, to find the maximum subtree depth after removal, we consider the max subtree depth for all nodes in the same level as the parent, and we adjust the subtree depth of the parent to be that of the its other child
# One issue is that we would have to do O(n) scans of levels, and levels can O(n) size, which could lead to O(n^2) performance
# A segtree would also work perfectly here, where the operation is the maximum
# If we knew the path to reach a particular node, we could do this easily: reach the node in log time, its subtree depth to 0 or -1 (something to act as if the subtree is remove), then recompute max for each parent node that contains the child node in one of its subtrees (also log time).  This would be O(n logn)
# Alternatively, the solution would work if we had a bool function is_in_subtree(parent, child) that answers in O(1) if node is in the subtree of another node
# Probably the path method is easier
# We can also just precompute for each node in some way, by tracking the highest and second highest depth for each level

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        heights = {}
        depths = {}
        def dfs(node, height):
            nonlocal heights, depths
            if node:
                depths[node.val] = height
                dfs(node.left, height + 1)
                dfs(node.right, height + 1)
                heights[node.val] = height
                if node.left:
                    heights[node.val] = max(heights[node.left.val], heights[node.val])
                if node.right:
                    heights[node.val] = max(heights[node.right.val], heights[node.val])
        dfs(root, 0)
        answers = {}
        q = deque([root])
        # print(heights)
        # print(depths)
        while q:
            n = len(q)
            best, second = -1, -1
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if n != 1:
                    if best == -1:
                        best = heights[node.val]
                    elif heights[node.val] >= best:
                        second = best
                        best = heights[node.val]
                    elif heights[node.val] > second:
                        second = heights[node.val]
            for node in level:
                if len(level) == 1:
                    answers[node.val] = depths[node.val] - 1
                elif best == second:
                    answers[node.val] = best
                elif heights[node.val] == best:
                    answers[node.val] = second
                else:
                    answers[node.val] = best
        res = []
        for query in queries:
            res.append(answers[query])
        return res