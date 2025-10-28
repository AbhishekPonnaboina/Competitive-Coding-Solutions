'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        #code here
        if not head:
            return None
        slow = head
        fast = head
        cnt = 0

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                fast = fast.next
                cnt += 1
                while fast is not slow:
                    fast = fast.next
                    cnt += 1
                break
                
            
        return cnt
        
    