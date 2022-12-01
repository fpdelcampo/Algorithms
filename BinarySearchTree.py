class BST:
    def __init__(self, data, left=None, right=None) -> None:
        self.left = left
        self.right = right
        self.data = data
    
def iterative_least_common_ancestor(root, n1, n2):
    while root!=None:
        if n1<root.left and n2<root.right:
            root=root.left

        elif n1>root.left and n2>root.right:
            root=root.right
        else:
            return root


def build(root, node): # Assumes uniqueness of values
    if root == None:
        return(node)
    elif node.data<root.data:
        root.left = build(root.left, node)
    else:
        root.right = build(root.right, node)

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