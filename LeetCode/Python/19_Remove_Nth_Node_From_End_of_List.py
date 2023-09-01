# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Say we have [1,2,3,4,5] and n = 2
# We want to reach 3 and then set 3.next = 3.next.next
# First we find out how many nodes there are, which we will call x
# If there are x nodes, we want to reach the x-n and set x-n.next = x-n.next.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next == None:
            return None
        count = 0
        copy = head
        while copy!=None:
            copy = copy.next
            count += 1
        if count == n:
            return head.next
        c = 0
        copy = head
        while c < count - n - 1:
            copy = copy.next
            c += 1
        if copy.next != None:
            copy.next = copy.next.next
        return head