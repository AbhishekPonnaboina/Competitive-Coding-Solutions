class Solution:
    def maxDepth(self, s: str) -> int:
        mystack = []
        maxdepth,currdepth = 0,0

        for i in s:
            if i == '(':
                mystack.append(i)
                currdepth += 1
            elif i == ')'  and mystack[-1] == '(':
                mystack.pop()
                currdepth -= 1 
            maxdepth = max(maxdepth,currdepth)
        return maxdepth