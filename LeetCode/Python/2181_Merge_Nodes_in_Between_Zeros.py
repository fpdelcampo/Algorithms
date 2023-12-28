# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        s = 0
        sentinel = ListNode(-1)
        copy = sentinel
        while curr.next:
            if curr.val:
                s += curr.val
            else:
                copy.next = ListNode(s)
                copy = copy.next
                s = 0
            curr = curr.next
        if curr.val:
            s += curr.val
        else:
            copy.next = ListNode(s)
            copy = copy.next
            s = 0
        return sentinel.next