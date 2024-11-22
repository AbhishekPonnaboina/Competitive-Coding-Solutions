# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head1 = list1
        head2 = list2
        curr = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
                              
            else:
                curr.next = head2
                head2 = head2.next
                curr = curr.next
        if head1:
            curr.next = head1
        else:
            curr.next = head2
        return dummy.next

















        """new_head = None
        curr1 = list1
        curr2 = list2

        if list1.val < list2.val :
            new_head = list1
            curr1 = curr1.next
        else:
            new_head = list2
            curr2 = curr2.next"""
        
        
        