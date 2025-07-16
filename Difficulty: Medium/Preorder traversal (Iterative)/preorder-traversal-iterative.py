'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    # Return a list containing the preorder traversal of the given tree
    def preOrder(self, ele):
        # code here
        if not ele:
            return []
        stack = [ele]
        res = []

        while stack:
            root = stack.pop()
            res.append(root.data)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            
        return res