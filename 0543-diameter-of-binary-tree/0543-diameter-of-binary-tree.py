# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if not root:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxi
        maxi = 0

        def maxiheight(root):
            if not root:
                return 0
            
            lh = maxiheight(root.left)
            rh = maxiheight(root.right)
            global maxi
            maxi = max(maxi,lh+rh)

            return 1 + max(lh,rh)

        maxiheight(root)
        return maxi