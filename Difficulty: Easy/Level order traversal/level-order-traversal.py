"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""

from collections import deque

class Solution:
    def levelOrder(self, root):
        # Your code here
        myque = deque([root])
        res = []
        
        while myque:
            lena = len(myque)
            lvl = []
            
            for i in range(lena):
                ele = myque.popleft()
                lvl.append(ele.data)
                
                if ele.left:
                    myque.append(ele.left)
                if ele.right:
                    myque.append(ele.right)
                    
                    
                    
            res.append(lvl)
        return res