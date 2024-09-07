# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        s = set(nums)
        cpy = head
        while cpy.val in s:
            cpy = cpy.next
        curr = cpy
        while curr:
            tail = curr.next
            while tail and tail.val in s:
                tail = tail.next
            curr.next = tail
            curr = curr.next
        return cpy
        
        
        
        
        
        
        
        
        
        
        
        
        # print(cpy.val)
        # while curr:
        #     print(curr.val)
        #     if not curr.next:
        #         break
        #     elif curr.next.val in s:
        #         print(f'found {curr.next.val}')
        #         curr.next = curr.next.next
        #     curr = curr.next
        # return cpy