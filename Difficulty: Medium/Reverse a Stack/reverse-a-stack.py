
class Solution:
    def reverse(self,St): 
        #code here
        
        
        def insertInStack(stack,ele):
            if not stack:
                stack.append(ele)
                return
            top = stack.pop()
            insertInStack(stack,ele)
            stack.append(top)
        
        
        def revStack(stack):
            if len(stack) <= 1:
                return 
            top = stack.pop()
            revStack(stack)
            insertInStack(stack,top)
            return stack
        
        
        
        
        return revStack(St)