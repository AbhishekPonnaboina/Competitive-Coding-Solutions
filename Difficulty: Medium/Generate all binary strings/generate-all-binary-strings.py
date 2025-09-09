#User function Template for python3

class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        
        def generateSubStrs(n,curr,res):
            if len(curr) == n:
                res.append(curr)
                return
            
            generateSubStrs(n,curr+"0",res)
            
            if not curr or curr[-1] != '1':
                generateSubStrs(n,curr+'1',res)
        
        curr = ''
        res = []
        generateSubStrs(n,curr,res)
        res.sort()
        return res