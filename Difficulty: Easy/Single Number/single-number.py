#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        xor = 0
        for i in arr:
            xor ^= i
        
        return xor
