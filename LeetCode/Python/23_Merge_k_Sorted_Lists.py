# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        for curr in lists:
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        sentinel = ListNode(-10001)
        curr = sentinel
        while heap:
            node = ListNode(heapq.heappop(heap))
            curr.next = node
            curr = curr.next
        return sentinel.next