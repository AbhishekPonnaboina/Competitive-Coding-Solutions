# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        curr = head
        size = 1
        while curr and curr.next:
            size += 1
            curr = curr.next
        curr.next = head
        
        k = k % size
        if k == 0:
            curr.next = None
            return head

        t = size - k - 1
        curr = head
        while t: 
            curr = curr.next
            t -= 1

        newhead = curr.next
        curr.next = None

        return newhead





        """if head is None:
            return None
        if k == 0:
            return head

        curr = head
        lena = 1
        while curr.next is not None:
            lena += 1
            curr = curr.next
        k = k % lena
        if k == 0:
            return head

        curr = head
        size = (lena - k) - 1
        while size:
            curr = curr.next
            size -= 1
        temp = ListNode()
        temp.next = curr.next
        curr.next = None
        curr2 = temp
        while curr2.next is not None:
            curr2 = curr2.next
        curr2.next = head
        return temp.next
"""

