'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
from collections import defaultdict,deque
class Solution:
    
    def verticalOrder(self, root): 
        #Your code here
        if not root:
            return []
        res = []
        myque = deque([(root,0,0)])
        mydict = defaultdict(list)
        index = 0
        
        while myque:
            root,row,col = myque.popleft()
            # mydict[col].append((row,root.data))
            mydict[col].append((row, index, root.data))
            
            if root.left:
                myque.append((root.left,row+1,col-1))
            if root.right:
                myque.append((root.right,row+1,col+1))
        
        # print(mydict)
        
        for i in sorted(mydict.keys()):
            laila = sorted(mydict[i],key=lambda x:(x[0],x[1]))
            res.append([val for row,idx,val in laila])
        
        
        
        return res
        
        
        
        
        
        
        
        
        
        
        