class Node:
    
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.nodes = 0
        self.k = k
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, value: int) -> bool:
        if self.nodes >= self.k:
            return False
        before = self.head
        after = self.head.next
        node = Node(value)
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node
        self.nodes += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.nodes >= self.k:
            return False
        before = self.tail.prev
        after = self.tail
        node = Node(value)
        node.prev = before
        node.next = after
        before.next = node
        after.prev = node
        self.nodes += 1
        return True

    def deleteFront(self) -> bool:
        if self.nodes == 0:
            return False
        node = self.head.next
        self.head.next = node.next
        node.next.prev = self.head
        del node
        self.nodes -= 1
        return True

    def deleteLast(self) -> bool:
        if self.nodes == 0:
            return False
        node = self.tail.prev
        self.tail.prev = node.prev
        node.prev.next = self.tail
        del node
        self.nodes -= 1
        return True

    def getFront(self) -> int:
        if self.head.next:
            return self.head.next.value
        return -1

    def getRear(self) -> int:
        if self.tail.prev:
            return self.tail.prev.value
        return -1

    def isEmpty(self) -> bool:
        return self.head.next == self.tail        

    def isFull(self) -> bool:
        return self.nodes == self.k

    def debug(self):
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()