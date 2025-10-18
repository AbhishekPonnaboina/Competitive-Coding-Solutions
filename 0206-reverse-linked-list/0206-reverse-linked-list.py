# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def recurrev(curr,prev):
            if not curr:
                return prev
            temp = curr.next
            curr.next = prev
            prev = curr
            return recurrev(temp,prev)
        
        return recurrev(head,None)


        





        # if not head:
        #     return 
        # prev = None
        # curr = head

        # temp = curr.next
        # curr.next = prev
        # prev = curr
        # curr = temp
        # if curr and curr.next:
        #     self.reverseList(curr.next)
        # return prev
        # if not head:
        #     return 
        # prev = None
        # curr = head

        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # return prev