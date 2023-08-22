class BSTNode:
    def __init__(self, data, left=None, right=None) -> None:
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root
    
    def insert(self, node): # Assumes uniqueness of values
        if self.root == None:
            self.root = node
        else:
            parent = None
            copy = self.root
            while copy != None:
                parent = copy
                if node.value < copy.value:
                    copy = copy.left
                else:
                    copy = copy.right
            if node.data < parent.data:
                parent.left = node
            else:
                parent.right = node
    
    def build(self, nodes): # Handles insertion of multiple nodes
        for node in nodes:
            self.insert(node)

    def delete(self, value):
        if self.root == None:
            return
        parent = None
        copy = self.root
        while copy.data != value:
            if copy.left == None and copy.right == None:
                return # Data not found
            parent = copy
            if value < self.copy.data:
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

            
        
        

    
def iterative_least_common_ancestor(root, n1, n2):
    while root!=None:
        if n1<root.left and n2<root.right:
            root=root.left

        elif n1>root.left and n2>root.right:
            root=root.right
        else:
            return root

def inorder(root, visited):
    if root.left!=None:
        inorder(root.left,visited)
    visited.append(root.data)
    if root.right!=None:
        inorder(root.right, visited)
    return visited

def main():
    nums = [i for i in range(100)]
    root = BST(nums[0])
    for i in range(1, len(nums)):
        build(root, BST(nums[i]))
    inorder_visited = inorder(root, [])
    print(inorder_visited)

if __name__ == "__main__":
    main()