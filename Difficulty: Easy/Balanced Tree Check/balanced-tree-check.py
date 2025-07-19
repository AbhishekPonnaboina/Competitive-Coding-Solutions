'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def isBalanced(self, root):
        # code here
        
        def modheight(root):
            if not root:
                return 0
            lh = modheight(root.left)
            if lh == -1:
                return -1
            rh = modheight(root.right)
            if rh == -1:
                return -1
            
            if abs(lh - rh) > 1:
                return -1
            return max(lh,rh) + 1
        
        
        