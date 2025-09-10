#User function Template for python3

class Solution:
    def subsets(self, arr):
        # code here
        n = len(arr)
        res = []
        
        subset = []
        
        def BackTracking(i):
            if i >= n:
                res.append(subset.copy())
                return
            subset.append(arr[i])
            BackTracking(i+1)
            
            subset.pop()
            BackTracking(i+1)
        
        BackTracking(0)
        res.sort()
        return res
            
