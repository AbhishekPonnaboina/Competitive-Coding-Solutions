#User function Template for python3

class Solution:
    
    # Function to find all combinations of elements
    # in array arr that sum to target.
    def uniqueCombinations(self, arr, k):
        # code here
        arr.sort()
        res = []
        n = len(arr)
        sub = []
        
        def generatesub(arr,sub,idx,suma):
            if suma == 0:
                res.append(sub.copy())
                return
            if suma < 0 or n == idx:
                return
            
            sub.append(arr[idx])
            generatesub(arr,sub,idx+1,suma-arr[idx])
            sub.pop()
            
            for j in range(idx+1,n):
                if arr[j] != arr[idx]:
                    generatesub(arr,sub,j,suma)
                    break
        
        generatesub(arr,sub,0,k)
        return res