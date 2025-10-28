'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def isPalindrome(self, head):
        # code here
        def reversehelpie(head):
            curr = head
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            return  prev
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = reversehelpie(slow.next)
        start = head
        
        while mid:
            if mid.data != start.data :
                reversehelpie(slow.next)
                return False
            start = start.next
            mid = mid.next
        else:
            reversehelpie(slow.next)
            return True
        