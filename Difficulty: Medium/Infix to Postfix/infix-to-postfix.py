#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        #code here
        stack = []
        operators = ['^','*','/','+','-']
        precedence = {'^': 4,'*': 3,'/': 3,'+': 2,'-': 2}
        def higher_precedence(op1, op2):
            if precedence[op1] < precedence[op2]:
                return 1
            elif precedence[op1] == precedence[op2]:
                return 0
            return -1
        res = ''
        
        for i in exp:
            if i.isalnum(): 
                res += i
            elif i == '(':
                    stack.append(i)
            elif i == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
                    
            elif i in operators:
                    while (stack and stack[-1] != '(' and
                       (higher_precedence(stack[-1], i) != 1 or
                        (i == '^' and precedence[stack[-1]] == precedence[i]))):
                        res += stack.pop()
                    stack.append(i)
                    
                                
        while stack:
            res += stack.pop()
        return res
                        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends