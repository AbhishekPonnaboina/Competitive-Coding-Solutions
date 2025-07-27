'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.

from collections import deque
class Solution:
    def LeftView(self, root):
        # code here
        myque = deque([root])
        
        res = []
        if not root:
            return res
        
        while myque:
            lela = len(myque)
            
            for i in range(lela):
                root = myque.popleft()
                if i == 0:
                    res.append(root.data)
                if root.left:
                    myque.append(root.left)
                if root.right:
                    myque.append(root.right)
        return res