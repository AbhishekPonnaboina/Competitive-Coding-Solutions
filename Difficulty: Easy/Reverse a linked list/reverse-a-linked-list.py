#function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        stack = []
        curr = head
        while curr:
            stack.append(curr.data)
            curr = curr.next
        curr = head
        while curr:
            curr.data = stack.pop()
            curr = curr.next
        return head



