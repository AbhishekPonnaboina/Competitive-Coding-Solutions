# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:        

        myqueue = deque([root])
        res1 = 0

        while myqueue:
            res1 = myqueue.popleft()
            if res1 is not None:
                if res1.right:
                    myqueue.append(res1.right)
    
                if res1.left:
                    myqueue.append(res1.left)
                   
        return res1.val
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """def leftordertraversal(root):
            if root.left is None:
                return root.val
            if root.left:
                return leftordertraversal(root.left)

        if root is None:
            return None
         
        res = leftordertraversal(root)
        return res"""