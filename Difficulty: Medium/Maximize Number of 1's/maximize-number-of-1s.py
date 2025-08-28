class Solution:
    def maxOnes(self, arr, k):
        # code here
        r,l = 0,0
        n =len(arr)
        zeros  = 0
        res = 0
        
        while r < n:
            if arr[r] == 0:
                zeros += 1
            
            while zeros > k:
                if arr[l] == 0:
                    zeros -= 1
                l += 1
            
            res = max(r-l+1,res)
            r += 1
        
        return res