# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        
        while head:
            res.append(head.val)
            head = head.next
        
        maxi = float("-inf")
        n = len(res)
        for i in range(len(res)//2):

            suma = res[i] + res[n-1-i]
            if suma > maxi:
                maxi = suma
        
        return  maxi