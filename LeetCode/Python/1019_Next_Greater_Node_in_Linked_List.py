# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        res = [0] * length
        i = 0
        while curr:  
            while stack and stack[-1][1] < curr.val:
                index, number = stack.pop()
                res[index] = curr.val            
            stack.append([i, curr.val])
            i += 1
            curr = curr.next
        return res