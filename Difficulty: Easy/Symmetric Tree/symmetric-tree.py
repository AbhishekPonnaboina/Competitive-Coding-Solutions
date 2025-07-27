'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def isSymmetric(self, root):
        #Code Here
        if not root:
            return True
        
        def dfs(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.data != root2.data:
                return False
            return dfs(root1.left,root2.right) and dfs(root1.right,root2.left)
        
        return dfs(root.left,root.right)