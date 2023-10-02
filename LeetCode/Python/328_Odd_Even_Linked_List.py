# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # So we basically create an odd linked list and an even linked list
    # Then we append the even list to the odd list
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        even = ListNode()
        copy = even
        prev_odd = None
        while odd:
            tmp = odd.next
            if odd.next:
                odd.next = odd.next.next
            if tmp:
                even.next = tmp
            else:
                even.next = None
            prev = odd
            odd = odd.next
            even = even.next
        prev.next = copy.next
        return head