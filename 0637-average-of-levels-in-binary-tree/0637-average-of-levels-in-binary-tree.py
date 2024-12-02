# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Que = deque([root])
        res = []

        while Que:
            level = []
            for i in range(len(Que)):
                curr = Que.popleft()
                level.append(curr.val)
                if curr.left:
                    Que.append(curr.left)
                if curr.right:
                    Que.append(curr.right)
            avg = sum(level) / len(level)
            res.append(avg)
            
        return res
        

                

        