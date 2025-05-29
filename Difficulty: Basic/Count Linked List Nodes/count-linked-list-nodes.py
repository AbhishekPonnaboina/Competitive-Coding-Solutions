'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        cnt = 0
        
        while head:
            head = head.next
            cnt += 1
        
        return cnt