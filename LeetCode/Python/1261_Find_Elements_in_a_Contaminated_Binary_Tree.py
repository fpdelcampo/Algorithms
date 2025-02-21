# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        values = set([])
        
        def fix(parent_value, node, is_left):
            nonlocal values
            if node:
                if is_left:
                    node.val = 2 * parent_value + 1
                else:
                    node.val = 2 * parent_value + 2
                values.add(node.val)
                fix(node.val, node.left, True)
                fix(node.val, node.right, False)

        if self.root:
            self.root.val = 0
            values.add(0)
            fix(self.root.val, self.root.left, True)
            fix(self.root.val, self.root.right, False)
        
        self.values = values

    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)