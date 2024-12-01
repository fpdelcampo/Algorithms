# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Preorder goes like:
# DFS(node):
# if node:
#       process(node)
#       dfs(node.left)
#       dfs(node.right)
# We process the node, then visit the left and right
# Some notes, if the last node has x dashes before it, and the current node has x + 1 dashes in front of it, then the current node is the left child of the previous node
# If the last node has x dashes and the current node has y dashes where y < x, then the current node is either the left child of the last node in the y-1th level, or if that node has a left node already, the right child.
# We can probably leverage the fact that to get to a node, we have to get to its parent
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dic = defaultdict(lambda: [])
        idx = 0
        last = -1
        while idx < len(traversal):
            depth = 0
            while traversal[idx + depth] == '-':
                # print('ahhhh')
                depth += 1
            value = ""
            value_length = 0
            while idx + depth + value_length < len(traversal) and traversal[idx + depth + value_length] != '-':
                value += traversal[idx + depth + value_length]
                value_length += 1
            # print(f"Started at {idx}, depth of {depth}, target is {value}")
            node = TreeNode(int(value))
            if last == -1:
                last = depth
                dic[0].append(node)
            else:
                # print(dic, depth - 1, depth -1 in dic)
                parent = dic[depth - 1][-1]
                if parent.left:
                    parent.right = node
                else:
                    parent.left = node
                dic[depth].append(node)
            last = depth
            idx += depth + value_length
        return dic[0][0]

        
        
        
        
        
        
        
        