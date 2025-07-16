# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        curr = root

        res = []
        stack = []

        while stack or curr:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if temp is None:
                    temp = stack.pop()
                    res.append(temp.val)
                    

                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.val)

                else:
                    curr = temp 
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """
        using two stacks
        if not root:
            return []

        stack1 = [root]
        stack2 = []

        while stack1:
            ele = stack1.pop()
            stack2.append(ele.val)
            if ele.left:
                stack1.append(ele.left)
            if ele.right:
                stack1.append(ele.right)
            
        
        return stack2[::-1]
        """
                