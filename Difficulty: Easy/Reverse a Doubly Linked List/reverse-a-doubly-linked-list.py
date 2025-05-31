#User function Template for python3

'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        if head is None:
            return None
        if head.next is None:
            return head
        else:
            curr = head
            temp = None
            while curr != None:
                temp = curr
                curr.next,curr.prev = curr.prev,curr.next
                curr = curr.prev
            return temp



