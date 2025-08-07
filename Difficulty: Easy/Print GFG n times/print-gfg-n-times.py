#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n == 0:
            return
        print("GFG",end=' ')
        return self.printGfg(n-1)
        