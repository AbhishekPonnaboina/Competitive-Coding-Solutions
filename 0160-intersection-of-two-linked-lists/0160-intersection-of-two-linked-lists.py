# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def helper(self,dist,small,large):
        """ this is for better approach which takes o(n) + o(2m)"""
        curr1 = large
        for i in range(dist):
            curr1 = curr1.next
        
        curr2 = small

        while curr1 and curr2 and curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
        
        if curr1:
            return curr1
        return 

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:return None

        l1 = l2 = 0

        curr1 = headA
        curr2 = headB

        while curr1:
            l1 += 1
            curr1 = curr1.next
        
        while curr2:
            curr2 = curr2.next
            l2 += 1
        
        if l1 > l2:
            return self.helper(l1-l2,headB,headA)
        else:
            return self.helper(l2-l1,headA,headB)













        #lala this is not working,extra space also
        # seta = set()
        # curr1 = headA
        # curr2 = headB

        # while curr1 or curr2:
        #     # print(seta)
        #     if curr1 and curr1 in seta:
        #         return curr1
        #     if curr2 and curr2 in seta:
        #         return curr2
            
            
        #     if curr1:
        #         seta.add(curr1)
        #         curr1 = curr1.next
        #     if curr2:
        #         seta.add(curr2)
        #         curr2 = curr2.next
        
        # return



    