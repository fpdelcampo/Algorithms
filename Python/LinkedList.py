class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, root=None) -> None:
        self.root = root
    
    def insert(self, node):
        if self.root == None:
            self.root = node
        else:
            copy = self.root
            while copy!=None:
                copy = copy.next
            copy.next = node
    
    def query(self, value):
        if self.root == None:
            return False
        copy = self.root
        while copy.next != None:
            copy=copy.next
        if copy.value == value:
            return True
        return False
    
def iterative_reverse(root):
    prev = None
    curr = root
    while curr!=None:
        after = curr.next
        curr.next = prev
        prev = curr   
        root = after
    return prev

def recursive_reverse(root):
    """
    
    Basically, start with the LL split like 0, 1..

    We place 0 at the end of 1.. and recursive swap 1..

    We do this for the whole LL
    
    """

    if root.next!=None:
        return root
    temp = root
    temp.next = recursive_reverse(root.next)
    return root

def is_cyclic(root):
    if root.next == None:
        return False
    copy = root.next
    while copy!=root and copy!=None:
        copy=copy.next
    if copy==None:
        return False
    return True

def main():
    pass

if __name__ == "__main__":
    main()