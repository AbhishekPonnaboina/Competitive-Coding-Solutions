'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        # Code here
        res = []
        
        if not root:
            return res
            
        def isLeafNode(root):
            return root and  not root.left and not root.right
        
        def leftBoundary(root):
            while root:
                if isLeafNode(root):
                    break
                res.append(root.data)
                if root.left:
                    root = root.left
                elif root.right:
                    root = root.right
            
        def inorder(root):
            if not root:
                return 
            if isLeafNode(root):
                res.append(root.data)
                return
            inorder(root.left)
            inorder(root.right)
        
        def rightBoundary(root):
            temp = []
            while root:
                if isLeafNode(root):
                    break
                temp.append(root.data)
                if root.right:
                    root = root.right
                elif root.left:
                    root = root.left
                
            res.extend(reversed(temp))
        
        if not isLeafNode(root):
            res.append(root.data)
        
        leftBoundary(root.left)
        inorder(root)
        rightBoundary(root.right)
        
        return res
            
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        