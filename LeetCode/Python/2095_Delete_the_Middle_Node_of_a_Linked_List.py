# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        length = 0 
        curr = head
        while curr:
            curr = curr.next
            length += 1
        index = 0
        middle = length // 2
        curr = head
        prev = None
        while index < middle:
            prev = curr
            curr = curr.next
            index += 1
        prev.next = curr.next
        return head