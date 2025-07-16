#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

# Return a list containing the inorder traversal of the given tree
class Solution:
    def inOrder(self, root):
        # code here
        ele = root
        stack = []
        res = []
        
        while True:
            if ele:
                stack.append(ele)
                ele = ele.left
            else:
                if not stack:
                    break
                ele = stack.pop()
                res.append(ele.data)
                ele = ele.right
        return res
    
                
        
        
        