# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #fast and slow pointer approach
        #tortoise and hoares method will identify the middle element
        #but we dont need the middle 
        #we need middle - 1
        # thats why we add an duplicate ele and then 
        #point from there
        if not head or not head.next:
            return 
        dummy = ListNode()
        dummy.next = head
        slow = dummy

        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        slow.next = slow.next.next
        
        return head



        #basic approach

        # if not head or not head.next:
        #     return
        
        # curr = head
        # lena = 0

        # while curr:
        #     curr = curr.next
        #     lena += 1
        # curr = head 
        # for i in range(lena//2 - 1):
        #     curr = curr.next
        
        # curr.next = curr.next.next
        # return head
