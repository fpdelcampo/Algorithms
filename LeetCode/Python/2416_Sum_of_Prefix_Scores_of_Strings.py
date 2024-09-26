# O(n^3) won't work here due to the input size.  The brute for is O(n^3), and it involves the following. Look at each word, for each prefix, match with other words in the array.
# We can maybe use a trie.  Idea is to build a trie with the property that each internal node also stores a value X that represents the number of leaf nodes with prefix corresponding to that internal node.  We then sum over all such values.
# After building the initial trie, I'm having a bit of trouble thinking about how to properly get the prefix_scores.
# If every word is marked by something like an is_word variable, then I could compute the number of words "below" a certain node.
# Consider the following trie:
#               '' 
#           /    |     
#         a      b (X)
#       /        |
#      ab (X)    bc (X)
#      /
#     abc (X)
# We can see that a should get a score of 2, ab, should get a score of 2, abc should get a score of 1, b should get a score of 2, bc should get a score of 2

class TrieNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children
        self.is_word = False
        self.score = 0

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    
    def build(self, words):
        for word in words:
            tmp = self.root
            for char in word:
                if tmp.children:
                    node = None
                    for child in tmp.children:
                        if child.value == char:
                            node = child
                    if not node:
                        node = TrieNode(char)
                        tmp.children.append(node)
                else:
                    node = TrieNode(char)
                    tmp.children = [node]
                tmp = node
                tmp.score += 1
            tmp.is_word = True
        
    def cumulative_score(self, word):
        # print(f'testing word {word}')
        total = 0
        tmp = self.root
        for char in word:
            for child in tmp.children:
                if char == child.value:
                    tmp = child
                    break
            total += child.score
            # print(f'last node\'s value was {child.value}, corresponding score was {child.score}')
            # print(f'after {char}, total is {total}')
        return total

    def display(self):
        q = deque([self.root])
        i = 0
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                print(f'Level {i} - {node.value} -> {node.score}')
                if node.children:
                    for child in node.children:
                        q.append(child)
            i += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        trie.build(words)
        res = []
        # trie.display()
        for word in words:
            res.append(trie.cumulative_score(word))
        return res