'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        res = []
        myque = deque([(root,0)])
        mydict = defaultdict(list)
        
        while myque:
            root,col = myque.popleft()
            mydict[col].append((root.data))
            
            if root.left:
                myque.append((root.left,col-1))
            if root.right:
                myque.append((root.right,col+1))
        
        # print(mydict)
        for i in sorted(mydict.keys()):
            res.append(mydict[i][-1])
        return res