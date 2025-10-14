'''
class Node:
    def _init_(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def mirror(self, root):
        # code here
        
        if not root:
            return None
        if root.left:
            self.mirror(root.left)
        if root.right:
            self.mirror(root.right)
        # if root.left and root.right:
        root.right,root.left = root.left,root.right

        return 