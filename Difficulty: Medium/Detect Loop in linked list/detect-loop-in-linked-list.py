#User function Template for python3
'''
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    
'''
# Return boolean value True or False

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        
        f = s = head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
            if s == f:
                return True
        return False
            
        
        
        
        


