# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        s1 = ListNode(-101)
        s2 = ListNode(-101)
        p1 = s1
        p2 = s2
        curr = head
        while curr:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next
            else:
                p2.next = curr
                p2 = p2.next
                print(p2.val, '>=')
            curr = curr.next
        p2.next = None
        p1.next = s2.next
        return s1.next