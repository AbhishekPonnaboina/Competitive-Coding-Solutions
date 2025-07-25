#User function Template for python3

class Solution:
    def removeOuter(self, S):
        # Code here
        
        MyStack = ''
        depth = 0
        
        for i in S:
            if i == '(':
                if depth > 0:
                    MyStack += i
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    MyStack += i
        return MyStack 
                