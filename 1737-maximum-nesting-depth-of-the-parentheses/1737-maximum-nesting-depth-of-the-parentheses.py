class Solution:
    def maxDepth(self, s: str) -> int:
        mystack = []
        res = 0

        for i in s:
            if i == '(':
                mystack.append(i)
            elif i == ')' and mystack and mystack[-1] == '(':
                mystack.pop()
                res = max(res,len(mystack)+1)
        return res