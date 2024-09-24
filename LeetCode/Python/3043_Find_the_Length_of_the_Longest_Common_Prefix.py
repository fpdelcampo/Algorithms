class Tree:
    def __init__(self, root):
        self.root = root

    def insert(self, str_number, first, second, add=False):
        tmp = self.root
        for i in str_number:
            node = None
            for child in tmp.children:
                if i == child.value:
                    node = child
            if node:
                if first and not node.first:
                    node.first = True
                if second and not node.second:
                    node.second = True
            else:
                node = Node(i, first, second)
                tmp.children.append(node)
            tmp = node

class Node:
    def __init__(self, value, first, second, children=None):
        self.value = value
        self.first = first
        self.second = second
        self.children = children if children is not None else []
    
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        tree = Tree(Node("", True, True))
        for num in arr1:
            tree.insert(str(num), True, False)
        for num in arr2:
            tree.insert(str(num), False, True)
        q = deque([tree.root])
        depth = 0
        res = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                if node.first and node.second:
                    if node.value != '':
                        res = max(res, depth)
                    for child in node.children:
                        q.append(child)
            depth += 1
        return res