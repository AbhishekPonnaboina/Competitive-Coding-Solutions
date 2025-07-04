# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        new_head = dummy
        curr1 = list1
        curr2 = list2

        while curr1 is not None and curr2 is not None:
            if curr1.val < curr2.val:
                new_head.next = curr1
                curr1 = curr1.next
            else:
                new_head.next = curr2
                curr2 = curr2.next
            new_head = new_head.next
        
        if curr1:
            new_head.next = curr1
        elif curr2:
            new_head.next = curr2
        return dummy.next