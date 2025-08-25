#User function Template for python3

class Solution:
    def maxDepth(self, s):
        # Code here
        currd,maxd = 0,0
        
        for i in s:
            if i == '(':
                currd += 1
            elif i == ')' :
                currd -= 1
            maxd = max(currd,maxd)
        
        return maxd