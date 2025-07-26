'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    #Function to return maximum path sum from any node in a tree.
    def findMaxSum(self, root): 
        #Your code here
        maxpath = [float('-inf')]
        
        def maxPathCal(root,maxpath):
            if not root:
                return 0
            lmax = max(maxPathCal(root.left,maxpath),0)
            rmax = max(maxPathCal(root.right,maxpath),0)
            maxpath[0] = max(maxpath[0],root.data+lmax+rmax)
            
            return root.data + max(lmax,rmax)
        
        maxPathCal(root,maxpath)
        
        return maxpath[0]