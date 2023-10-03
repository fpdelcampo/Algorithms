# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Need to passes for the case 999999999 etc.
    def plusOne(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        nine = False
        nine_root = None
        all_nines = True

        while curr:
            if curr.val == 9 and not nine:
                nine_root = prev
                nine = True
            elif curr.val != 9:
                nine_root = None
                nine = False
                all_nines = False
            prev = curr
            curr = curr.next
        
        if nine_root: 
            nine_root.val += 1
            nine_root = nine_root.next
            while nine_root:
                nine_root.val = 0
                nine_root = nine_root.next
            return head
        else:
            if all_nines: # All 9s
                new_head = ListNode(1, head)
                while head:
                    head.val = 0
                    head = head.next
                return new_head
            else:
                prev.val += 1
                return head