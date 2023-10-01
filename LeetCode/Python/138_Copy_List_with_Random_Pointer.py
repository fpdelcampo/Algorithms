"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # Time O(n), space O(n)
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    #     if not head:
    #         return None
    #     nodes = {} # val : new_node
    #     original = head
    #     copy = Node(head.val)
    #     nodes[head] = copy    
    #     while original != None:
    #         if original.next in nodes:
    #             copy.next = nodes[original.next]
    #         elif original.next is None:
    #             copy.next = None
    #         else:
    #             nodes[original.next] = Node(original.next.val)
    #             copy.next = nodes[original.next]
            
    #         if original.random is None:
    #             copy.random = None
    #         elif original.random in nodes:
    #             copy.random = nodes[original.random]
    #         else:
    #             nodes[original.random] = Node(original.random.val)
    #             copy.random = nodes[original.random]
    #         copy = copy.next
    #         original = original.next
    #     return nodes[head]

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        if not head.next:
            if not head.random:
                return Node(head.val, None, None)
            else:
                tmp = Node(head.val)
                tmp.random = tmp
                return tmp
        curr = head
        while curr != None:
            tmp = Node(curr.val)
            after = curr.next
            curr.next = tmp
            curr.next.next = after
            curr = curr.next.next
        
        curr = head
        while curr != None:
            new = curr.next
            if curr.random is None:
                new.random = None
            else:
                new.random = curr.random.next
            curr = curr.next.next
        
        copy = head.next
        curr = head.next
        while curr != None:
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            curr = curr.next
        return copy