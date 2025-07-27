# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        mydict = defaultdict(list)
        myque = deque([(root,0)])

        while myque:
            root,row = myque.popleft()
            mydict[row].append(root.val)
            if root.left:
                myque.append((root.left,row+1))
            if root.right:
                myque.append((root.right,row+1))
        print(mydict)
        for i in sorted(mydict.keys()):
            res.append(mydict[i][-1])
        return res

