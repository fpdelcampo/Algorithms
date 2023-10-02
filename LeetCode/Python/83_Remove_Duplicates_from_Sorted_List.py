# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        last = -101
        while curr != None:
            last = curr.val
            copy = curr
            while curr is not None and curr.val == last:
                curr = curr.next
            copy.next = curr
        return head