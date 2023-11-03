class Node:
    def __init__(self, val, children, is_leaf):
        self.val = val
        self.children = children
        self.is_leaf = is_leaf

class WordDictionary:

    def __init__(self):
        self.root = Node("", [], False)

    def addWord(self, word: str) -> None:
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
        def recSearch(root, word, idx):
            if idx == len(word):
                return root.is_leaf
            if word[idx] == '.':
                for child in root.children:
                    if recSearch(child, word, idx+1):
                        return True
                return False
            for child in root.children:
                if word[idx] == child.val:
                    return recSearch(child, word, idx+1)
            return False
        return recSearch(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)