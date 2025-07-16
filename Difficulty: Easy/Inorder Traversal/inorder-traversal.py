'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        
        res  = []
        def inorder(root,res):
            if not root:
                return 
            inorder(root.left,res)
            res.append(root.data)
            inorder(root.right,res)
        
        inorder(root,res)
        return res