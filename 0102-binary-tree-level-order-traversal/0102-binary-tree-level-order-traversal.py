from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que1 =  deque([root])
        que2 = deque()
        res = []
        res2 = []


        while que1:
            ele = que1.popleft()
            res2.append(ele.val)            
            if ele.left:
                que2.append(ele.left)
            if ele.right:
                que2.append(ele.right)
            if not que1:
                res.append(res2)
                res2 = []
                que1,que2= que2,que1


        return res