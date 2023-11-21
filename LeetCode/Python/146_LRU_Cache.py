class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.kv = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, key, val):
        node = Node(key, val)
        second = self.head.next
        second.prev = node
        node.next = second
        node.prev = self.head
        self.head.next = node
        
    def get(self, key: int) -> int:
        if key not in self.kv:
            return -1
        val = self.kv[key].val
        self.remove(self.kv[key])
        self.add(key, val)
        self.kv[key] = self.head.next
        return self.kv[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.remove(self.kv[key])
            self.add(key, value)
            self.kv[key] = self.head.next
        else:
            if len(self.kv) >= self.capacity:
                del self.kv[self.tail.prev.key]
                self.remove(self.tail.prev)
            self.add(key, value)
            self.kv[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)