'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def detectLoop(self, head):
        # code here
        
        if not head:
            return
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next 
            slow = slow.next
            if fast is slow:
                return True
        
        if slow != fast:
            return False
