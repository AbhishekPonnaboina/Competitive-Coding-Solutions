# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB
        lena1 = 0
        while curr1:
            lena1 += 1
            curr1 = curr1.next
        lena2 = 0
        while curr2:
            lena2 += 1
            curr2 = curr2.next
        curr1 = headA
        curr2 = headB
        diff = abs(lena1 - lena2)
        for i in range(diff):
            if lena1 > lena2:
                curr1 = curr1.next
            else:
                curr2 = curr2.next
        while curr1 and curr2:
            if curr1 == curr2:
                return curr1
            curr1 = curr1.next
            curr2 = curr2.next
        return None



        