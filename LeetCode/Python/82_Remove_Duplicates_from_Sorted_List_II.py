# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # This gives time O(n) and space O(n), but we can get it down to O(1) space
    # seen = set()
    # dup = set()
    # curr = head
    # prev = None
    # while curr != None:
    #     if curr.val in seen and curr.val not in dup:
    #         dup.add(curr.val)
    #     seen.add(curr.val)
    #     curr = curr.next
    # curr = head
    # print(dup)
    # while curr != None and curr.val in dup:
    #     curr = curr.next

    # copy = curr
    # while copy != None:
    #     if copy.val in dup:
    #         prev.next = copy.next
    #     else:
    #         prev = copy
    #     copy = copy.next
    # return curr
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(-101, head)
        curr = head
        prev = sentinel
        last = -101
        while curr is not None:
            if (curr.next and curr.val == curr.next.val) or curr.val == last:
                prev.next = curr.next
            else:
                prev = curr
            last = curr.val
            curr = curr.next
        return sentinel.next

        