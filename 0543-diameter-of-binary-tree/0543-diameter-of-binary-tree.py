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
        if not root:
            return  0
        d1 =  self.height(root.left) + self.height(root.right)
        d2 =   self.diameterOfBinaryTree(root.left)
        d3 = self.diameterOfBinaryTree(root.right)

        return max(d1,d2,d3)