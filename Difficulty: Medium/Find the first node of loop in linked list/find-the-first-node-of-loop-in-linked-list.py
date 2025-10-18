"""
class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
"""

class Solution:
    def cycleStart(self, head):
        #code here
        #done in the leetcode with the proof and two approaches
        
        if not head:
            return -1
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                slow = head
                
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                
                return fast.data
            
        return -1
        