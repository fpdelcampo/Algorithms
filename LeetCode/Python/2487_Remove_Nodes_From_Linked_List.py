# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        sentinel = ListNode(-1)
        curr = head
        while curr:
            while stack and stack[-1] < curr.val:
                stack.pop()
            stack.append(curr.val)
            curr = curr.next
        curr = sentinel
        for i in range(len(stack)):
            node = ListNode(stack[i])
            curr.next = node
            curr = curr.next
        return sentinel.next