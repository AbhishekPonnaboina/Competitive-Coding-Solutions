# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """def height(self,root):
            if not root:
                return 0
            return max(self.height(root.left),self.height(root.right)) + 1
        
        """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
    
        def modheight(root):
            if not root:
                return 0
            
            left = modheight(root.left)
            if left == -1:
                return -1
            right = modheight(root.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return max(left,right) + 1
        
        if modheight(root) == -1:
            return False
        return True
        









        
        """if not root:
            return True
        left = self.height(root.left)
        right = self.height(root.right)

        return abs(left-right) <= 1 and self.isBalanced(root.left) and  self.isBalanced(root.right)"""