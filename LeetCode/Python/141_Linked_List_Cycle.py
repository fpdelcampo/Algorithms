# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast = head
        skip = True
        while curr is not None and fast is not None:
            if not skip:
                if curr == fast:
                    return True
            else:
                skip = False
            curr = curr.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
        return False
        

        