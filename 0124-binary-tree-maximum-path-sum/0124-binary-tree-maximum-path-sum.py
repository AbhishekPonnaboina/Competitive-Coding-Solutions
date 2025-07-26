# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxi = [float('-inf')]

        def maxpath(root,maxi):
            if not root:
                return 0
            lmax = max(maxpath(root.left,maxi),0)
            rmax = max(maxpath(root.right,maxi),0)

            maxi[0] = max(maxi[0],root.val+lmax+rmax)
            
            branch = root.val + max(lmax,rmax)
            return branch 
        maxpath(root,maxi)
        return maxi[0]