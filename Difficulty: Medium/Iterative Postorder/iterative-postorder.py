#User function Template for python3

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    # Return a list containing the post order traversal of the given tree
    def postOrder(self,root):
        # code here
        curr = root
        if not root:
            return []
        res = []
        stack = []
        
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    res.append(temp.data)
                    
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.data)
                    
                else:
                    curr = temp
        return res        
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                
                