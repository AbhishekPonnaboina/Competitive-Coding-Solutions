# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def inverttreerec(root):
            if not root:
                return None
            if root.left:
                inverttreerec(root.left)
            if root.right:
                inverttreerec(root.right)
            root.left , root.right = root.right,root.left
            return
        
        inverttreerec(root)
        return root








        # mydeque = deque()
        # if root:
        #     mydeque.append(root)
        # res = []

        # while mydeque:
        #     ele = mydeque.popleft()
        #     res.append(ele.val)
        #     if ele.left:
        #         mydeque.append(ele.left)
        #     if ele.right:
        #         mydeque.append(ele.right)
        

        # for i in range(0,len(res)-2,2):
        #     res[i+1],res[i+2] = res[i+2],res[i+1]

        # print(*res)    
        return