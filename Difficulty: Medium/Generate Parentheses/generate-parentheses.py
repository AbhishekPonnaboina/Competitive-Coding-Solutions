#User function Template for python3

class Solution:
    def generateParentheses(self, n):
        #code here
        res = []
        n = n // 2
        def generate(mystr,Open,Close,n):
            if 2*n == len(mystr):
                res.append(mystr)
                return
            if Open < n:
                generate(mystr+"(",Open+1,Close,n)
            if Close < Open:
                generate(mystr+")",Open,Close+1,n)
        
        mystr = ""
        generate(mystr,0,0,n)
        return res