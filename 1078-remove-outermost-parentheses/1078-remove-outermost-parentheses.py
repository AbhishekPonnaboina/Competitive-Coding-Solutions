class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        MyStack = ''
        FirstCount = 0
        SecondCount = 0
        res = ''

        for i in s:
            print(MyStack)
            if i == '(':
                MyStack += i
                FirstCount += 1
                
            elif i == ")":
                if FirstCount - 1 != SecondCount:
                    MyStack += i
                    SecondCount += 1
                else:
                    res += MyStack[1:]
                    MyStack = ''
                    FirstCount = 0
                    SecondCount = 0
        return res




