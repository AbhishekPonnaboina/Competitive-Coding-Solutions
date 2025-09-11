#User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def combinationSum(self, arr, k):
        # code here
        
        res = []
        sub = []
        n = len(arr)
        
        def generatesub(arr,sub,idx,suma):
            if suma == 0:
                res.append(sub.copy())
                return
            
            if suma < 0 or n == idx:
                return 
            
            sub.append(arr[idx])
            generatesub(arr,sub,idx,suma - arr[idx])
            sub.pop()
            generatesub(arr,sub,idx+1,suma)
        
        generatesub(arr,sub,0,k)
        
        return res