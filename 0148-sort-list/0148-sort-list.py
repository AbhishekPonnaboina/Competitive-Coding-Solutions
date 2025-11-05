# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #basic approach clears this but there is follow up O(nlogn) and O(1) space?
        #space - o(n)
        #time = o(n) + o(nlogn)
        #how not to use the memory here?
        # i can some how do the buble sort version for this
        #but we know that its worst complexity is o(n^2)
        #so how to do in nlogn
        #bro you dont need extra space to change the links its just easy
        # so implement the merge sort
        

        if not head or not head.next:
            return head
        
        middle = self.getmiddle(head)
        righthead = head
        lefthead = middle.next
        middle.next = None
        newright = self.sortList(righthead)
        newleft = self.sortList(lefthead)

        return self.mergeList(newright,newleft)       

    def mergeList(self,right,left):
        curr1 = right
        curr2 = left
        dummy = ListNode(-1)
        head = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                dummy.next = curr1
                curr1 = curr1.next
            else:
                dummy.next = curr2
                curr2 = curr2.next
            dummy = dummy.next
        if curr1:
            dummy.next = curr1
        elif curr2:
            dummy.next = curr2
        
        return head.next

    def getmiddle(self,head):
        if not head:
            return 
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        #basic approach
        # mylist = []
        
        # if not head:
        #     return
        # curr = head

        # while curr:
        #     mylist.append(curr.val)
        #     curr = curr.next
        
        # mylist.sort(reverse=True)

        # curr = head

        # while curr:
        #     curr.val = mylist.pop()
        #     curr = curr.next
        
        # return head
        