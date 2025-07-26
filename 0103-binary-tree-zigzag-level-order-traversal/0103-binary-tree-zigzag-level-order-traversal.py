# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        myDeque = deque([root])
        resArr = []
        i = 0
        while myDeque:
            tempArr = []            
            x = len(myDeque) 
            for _ in range(x):
                ele = myDeque.popleft()
                if ele.left:
                    myDeque.append(ele.left)
                if ele.right:
                    myDeque.append(ele.right)
                tempArr.append(ele.val)
            if i % 2 != 0:
                resArr.append(tempArr[::-1])
            else:
                resArr.append(tempArr)
            i += 1
        return resArr                
            
