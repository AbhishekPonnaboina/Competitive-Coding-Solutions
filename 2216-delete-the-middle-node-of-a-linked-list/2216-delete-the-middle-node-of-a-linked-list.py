# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #basic approach

        if not head or not head.next:
            return
        
        curr = head
        lena = 0

        while curr:
            curr = curr.next
            lena += 1
        curr = head 
        for i in range(lena//2 - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        return head
