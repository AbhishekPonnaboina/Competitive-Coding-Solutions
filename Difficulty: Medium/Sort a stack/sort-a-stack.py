class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack

    
    def Sorted(self, s):
        # Code here
        def insertAtCorrect(stack,ele):
            if not stack or stack[-1] <= ele:
                stack.append(ele)
                return
            top = stack.pop()
            insertAtCorrect(stack,ele)
            stack.append(top)
            
        
        def sortstack(stack):
            if len(stack) <= 1:
                return 
            top = stack.pop()
            sortstack(stack)
            insertAtCorrect(stack,top)
            return stack
        
        return sortstack(s)
        

