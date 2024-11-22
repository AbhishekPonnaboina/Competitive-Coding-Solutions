# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None


        while head and head.val == val:
            head = head.next
        if head is None:
            return None
       
        curr = head       

        while curr:
            temp = curr.next
            while temp and temp.val == val:
                    temp = temp.next
            curr.next = temp
            curr = curr.next

        return head

            
