'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
#Function to return a list containing the preorder traversal of the tree.
    def preorder(self,root):
        res = []

        def preorder(root,res):
            if root == None:
                return 
            res.append(root.data)
            preorder(root.left,res)
            preorder(root.right,res)
        
        preorder(root,res)
        return res
        
        
   
    # code here