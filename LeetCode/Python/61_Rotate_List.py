# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        prev = None
        curr = head
        length = 0
        while curr:
            length += 1
            prev = curr
            curr = curr.next
        last = prev
        curr = head
        idx = 1
        k = k % length
        if k == 0:
            return head 
        while idx < length - k:
            idx += 1
            curr = curr.next
        start = curr.next
        curr.next = None
        last.next = head
        return start