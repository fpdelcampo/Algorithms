class Node:
    def __init__(self, val, children, is_leaf):
        self.val = val
        self.children = children
        self.is_leaf = is_leaf

class Trie:
    def __init__(self):
        self.root = Node("", [], False)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            match = False
            for child in curr.children:
                if char == child.val:
                    curr = child
                    match = True
                    break
            if not match:
                node = Node(char, [], False)
                curr.children.append(node)
                curr = node
        curr.is_leaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            match = False
            for child in curr.children:
                if char == child.val:
                    curr = child
                    match = True
                    break
            if not match:
                return False
        return curr.is_leaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            match = False
            for child in curr.children:
                if char == child.val:
                    curr = child
                    match = True
                    break
            if not match:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)