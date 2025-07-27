# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        mydict = defaultdict(list)
        queue = deque([(root,0,0)])
        # print(queue)

        while queue:
            root,row,col = queue.popleft()
            mydict[col].append((row,root.val))
            if root.left:
                queue.append((root.left,row+1,col-1))
            if root.right:
                queue.append((root.right,row+1,col+1))
        
        # print(mydict)
        for i in sorted(mydict.keys()):
            col = sorted(mydict[i],key =  lambda x:(x[0],x[1]))
            res.append([val for row,val in col])
        return res
        
