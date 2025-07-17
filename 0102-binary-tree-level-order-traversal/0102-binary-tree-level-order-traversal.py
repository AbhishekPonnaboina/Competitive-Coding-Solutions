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
        que =  deque([root])
        res = []
        

        while que:
            lvsize = len(que)
            level = []

            for i in range(lvsize):
                ele = que.popleft()
                level.append(ele.val)

                if ele.left:
                    que.append(ele.left)
                if ele.right:
                    que.append(ele.right)
            res.append(level)
        return res