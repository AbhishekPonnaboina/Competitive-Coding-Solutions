# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:


            res = []

            def inordertrav(root):
                if root is None :
                    return 
                else:
                    inordertrav(root.left)
                    res.append(root.val)
                    inordertrav(root.right)
            inordertrav(root)
            return res