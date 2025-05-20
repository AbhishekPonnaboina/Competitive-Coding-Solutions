#User function Template for python3


class Solution:
    def findMissing(self, arr1,arr2):
        # code here
        xor1 = 0
        xor2 = 0
        
        for i in arr1:
            xor1 = xor1 ^ i
        
        for i in arr2:
            xor2 = xor2 ^ i
        
        return xor1 ^ xor2
    
