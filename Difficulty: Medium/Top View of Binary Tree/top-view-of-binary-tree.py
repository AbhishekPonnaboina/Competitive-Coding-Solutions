# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
from collections import deque,defaultdict
class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        if not root:
            return []
        res = []
        myque = deque([(root,0,0)])
        mydict = defaultdict(list)
        
        while myque:
            root,row,col = myque.popleft()
            mydict[col].append((row,root.data))
            
            if root.left:
                myque.append((root.left,row+1,col-1))
            if root.right:
                myque.append((root.right,row+1,col+1))
        
        # print(mydict)
        for i in sorted(mydict.keys()):
            res.append(mydict[i][0][1])
        return res
        
        