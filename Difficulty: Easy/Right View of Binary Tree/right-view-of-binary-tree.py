'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque
class Solution:
    #Function to return list containing elements of right view of binary tree.
    def rightView(self,root):
        
        # code here
        myque = deque([root])
        res = []
        
        while myque:
            lvlsize = len(myque)
            
            for i in range(lvlsize):
                root = myque.popleft()
                if i == lvlsize - 1:
                    res.append(root.data)
                if root.left:
                    myque.append(root.left)
                if root.right:
                    myque.append(root.right)
        return res
                
        