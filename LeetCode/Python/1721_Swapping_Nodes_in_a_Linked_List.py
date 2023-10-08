# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        length = 1
        first = None
        while curr:
            if length == k:
                first = curr
            length += 1
            curr = curr.next
        # length represents the number of nodes in the array plus one, so we adjust after a simple check
        length -= 1
        second = None
        curr = head
        idx = 1
        while idx <= length - k:
            idx += 1
            curr = curr.next
        second = curr
        first.val, second.val = second.val, first.val
        return head