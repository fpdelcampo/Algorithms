class BSTNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
    
    def insert(self, node): # Assumes uniqueness of values
        if self.root == None:
            self.root = node
        else:
            parent = None
            copy = self.root
            while copy != None:
                parent = copy
                if node.data < copy.data:
                    copy = copy.left
                else:
                    copy = copy.right
            if node.data < parent.data:
                parent.left = node
            else:
                parent.right = node
    
    def build(self, nodes): # Handles insertion of multiple nodes
        for node in nodes:
            self.insert(BSTNode(node))

    def delete(self, value):
        if self.root == None:
            return
        parent = None
        copy = self.root
        while copy.data != value:
            if copy.left == None and copy.right == None:
                return # Data not found
            parent = copy
            if value < copy.data:
                copy = copy.left
            else:
                copy = copy.right
        num_matches = 0
        
        if copy.left != None:
            num_matches += 1
        if copy.right != None:
            num_matches += 1
        
        if num_matches == 0:
            if parent.left == value:
                parent.left = None
            else:
                parent.right = None
        elif num_matches == 1:
            if parent.left == value:
                parent.left = copy.left
            else:
                parent.right = copy.right
        else:
            tracker = copy
            print(tracker.data,"+++")
            print(copy.data,"----")
            while tracker.right != None:
                tracker.data = tracker.right.data
                tracker = tracker.right
            tracker = None
    
    def inorder(self):
        visited = []
        visited = self.inorder_recursive(self.root, visited)
        return visited
    
    def inorder_recursive(self, node, visited):
        if node == None:
            return
        self.inorder_recursive(node.left, visited)
        visited.append(node.data)
        self.inorder_recursive(node.right, visited)

    def preorder(self):
        visited = self.preorder_recursive(self.root, [])
        return visited
    
    def preorder_recursive(self, node, visited):
        if node == None:
            return
        visited.append(node.data)
        self.preorder_recursive(node.left, visited)
        self.preorder_recursive(node.right, visited)
        return visited
    
    def postorder(self):
        visited = self.postorder_recursive(self.root, [])
        return visited
    
    def postorder_recursive(self, node, visited):
        if node == None:
            return
        self.postorder_recursive(node.left, visited)
        self.postorder_recursive(node.right, visited)
        visited.append(node.data)

    def iterative_least_common_ancestor(self, n1, n2):
        copy = self.root
        while copy != None:
            if n1 < copy.left.data and n2<copy.right.data:
                copy = copy.left

            elif n1>copy.left.data and n2>copy.right.data:
                copy = copy.right
            else:
                return copy.data
def display(list_of_nodes):
    for node in list_of_nodes:
        print(node.data or node)
            
def test_bst_methods():
    # Create a BST and insert values
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    bst.build(values)
    
    print(bst.root.data)

    print(bst.root.left.data, bst.root.right.data)

    print(bst.root.left.left.data, bst.root.left.right.data, '/', bst.root.right.left.data, bst.root.right.right.data)
    
    bst.delete(70)

    print(bst.root.data)

    print(bst.root.left.data, bst.root.right.data)

    print(bst.root.left.left.data, bst.root.left.right.data, '/', bst.root.right.left.data)


if __name__ == "__main__":
    test_bst_methods()