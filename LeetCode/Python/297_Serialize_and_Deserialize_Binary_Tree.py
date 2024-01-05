# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # Need to use a level order approach
    def serialize(self, root):
        if not root:
            return ""
        res = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node:
                empty = False
                q.append(node.left)
                q.append(node.right)
                res.append(str(node.val))
            else:
                res.append('null')
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        tmp = iter(data.split(','))
        root = TreeNode(int(next(tmp)))
        q = deque()
        q.append(root)
        while q:
            iters = len(q)
            for _ in range(iters):
                node = q.popleft()
                l = next(tmp)
                r = next(tmp)
                if l != 'null':
                    node.left = TreeNode(int(l))
                    q.append(node.left)
             
                if r != 'null':
                    node.right = TreeNode(int(r))
                    q.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))