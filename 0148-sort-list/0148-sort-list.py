# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        



        #basic approach
        mylist = []
        
        if not head:
            return
        curr = head

        while curr:
            mylist.append(curr.val)
            curr = curr.next
        
        mylist.sort(reverse=True)

        curr = head

        while curr:
            curr.val = mylist.pop()
            curr = curr.next
        
        return head
        