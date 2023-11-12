# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)
        i = 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, i, head))
                i += 1
        sentinel = ListNode(-10001)
        curr = sentinel
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                i += 1
            curr = curr.next
        return sentinel.next