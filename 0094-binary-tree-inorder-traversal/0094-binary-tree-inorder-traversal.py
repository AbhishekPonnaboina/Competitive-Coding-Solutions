
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        stack = []
        ele = root
        res = []


        while True:
            if ele:
                stack.append(ele)
                ele = ele.left
            else:
                if not stack:
                    break
                ele = stack.pop()
                res.append(ele.val)
                ele = ele.right
        
        return res


            

                
            
        
        return res
