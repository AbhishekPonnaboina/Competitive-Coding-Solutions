'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        # code here
        res = []
        
        def postorder(root,res):
            if not root:
                return 
            postorder(root.left,res)
            postorder(root.right,res)
            res.append(root.data)
        postorder(root,res)
        return res