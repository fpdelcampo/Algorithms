# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next
        curr = head
        best = 0
        for i in range(len(stack) // 2):
            best = max(best, curr.val + stack[-1])
            stack.pop()
            curr = curr.next
        return best