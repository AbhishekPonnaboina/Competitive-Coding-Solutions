'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        # Your code here
        
        global maxi
        maxi = 0
        
        def height(root):
            if not root:
                return 0
                
            lh = height(root.left)
            rh = height(root.right)
            
            global maxi
            
            maxi = max(maxi,lh+rh)
            
            return max(lh,rh)+1
        
        height(root)
        return maxi