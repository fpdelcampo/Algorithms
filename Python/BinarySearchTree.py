class BSTNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, root=None):
        self.root = root
        self.visited = []
    
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

    def isin(self, value):
        copy = self.root
        if self.root.data == value:
            return True
        while copy.left is not None and copy.right is not None:
            if value < copy.data:
                copy = copy.left
            else:
                copy = copy.right
            if copy.data == value:
                return True
        return False

    def delete(self, value): # Assumes value is in the BST
        if self.root == None:
            return
        
        parent = None
        copy = self.root

        print(f"{self.root.data} //// ")
        while copy.data != value:
            parent = copy
            if value < copy.data:
                copy = copy.left
            else:
                copy = copy.right
        
        num = self.leaves(value)
        
        if num == 0:
            if self.root.data == value:
                self.root = None
            elif parent.left is not None and parent.left.data == value:
                parent.left = None
            else:
                parent.right = None
        
        elif num == 1:
            if parent == None:
                self.root = copy.left if copy.left is not None else copy.right
            elif parent.left == copy:
                parent.left = copy.left if copy.left is not None else copy.right
            else:
                parent.right = copy.left if copy.left is not None else copy.right
        
        else:
            # here the goal is to swap the value with the inorder successor's value, and then delete the inorder successor
            # to do this, we need to find the parent of the inorder successor and the inorder successor
            # copy.value = value, so we will start at copy
            c = copy
            p = None
            first = True
            while c.left is not None:
                p = c
                if first:
                    c = c.right
                    first = False
                else:
                    c = c.left
            copy.data = c.data
            if p.left.data == copy.data:
                p.left = p.left.right
            else:
                p.right = p.right.right     
        
    def leaves(self, value): # Assumes the value is in the BST
        copy = self.root
        while copy.data != value:
            if value < copy.data:
                copy = copy.left
            else:
                copy = copy.right
        num = 0
        if copy.left is not None:
            num+=1
        if copy.right is not None:
            num+=1
        return num

    def inorder(self):
        self.visited = []
        self.inorder_recursive(self.root)
    
    def inorder_recursive(self, node):
        if node == None:
            return
        self.inorder_recursive(node.left)
        self.visited.append(node.data)
        self.inorder_recursive(node.right)

    def preorder(self):
        self.visited = []
        self.preorder_recursive(self.root)
    
    def preorder_recursive(self, node):
        if node == None:
            return
        self.visited.append(node.data)
        self.preorder_recursive(node.left)
        self.preorder_recursive(node.right)
    
    def postorder(self):
        self.visited = []
        self.postorder_recursive(self.root)

    def postorder_recursive(self, node):
        if node == None:
            return
        self.postorder_recursive(node.left)
        self.postorder_recursive(node.right)
        self.visited.append(node.data)

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
            
def main():
    # Create a BST and insert values
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    bst.build(values)

    # Test deleting a leaf (20)
    bst.delete(20)
    expected_inorder = [30, 40, 50, 60, 70, 80]
    bst.inorder()
    actual_inorder = bst.visited
    assert expected_inorder == actual_inorder, "Deletion of leaf node failed!"

    # Test deleting a node with one child (60)
    bst.delete(60)
    expected_inorder = [30, 40, 50, 70, 80]
    bst.inorder()
    actual_inorder = bst.visited
    assert expected_inorder == actual_inorder, "Deletion of node with one child failed!"

    # Test deleting a node with two children (50)
    bst.delete(50)
    expected_inorder = [30, 40, 70, 80]
    bst.inorder()
    actual_inorder = bst.visited
    assert expected_inorder == actual_inorder, "Deletion of node with two children failed!"

    # Test deleting root node (30)
    bst.delete(30)
    expected_inorder = [40, 70, 80]
    bst.inorder()
    print(bst.visited)

    actual_inorder = bst.visited
    assert expected_inorder == actual_inorder, "Deletion of root node failed!"

    bst = BST()
    bst.build([50, 30, 70, 20, 40, 60, 80])

    expected_inorder = [20, 30, 40, 50, 60, 70, 80]
    bst.inorder()
    actual_inorder = bst.visited
    assert expected_inorder == actual_inorder, "Inorder failed!"

    expected_preorder = [50, 30, 20, 40, 70, 60, 80]
    bst.preorder()
    actual_preorder = bst.visited
    assert expected_preorder == actual_preorder, "Preorder failed!"

    expected_postorder = [20, 40, 30, 60, 80, 70, 50]
    bst.postorder()
    actual_postorder = bst.visited
    assert expected_postorder == actual_postorder, "Inorder failed!"


if __name__ == "__main__":
    main()