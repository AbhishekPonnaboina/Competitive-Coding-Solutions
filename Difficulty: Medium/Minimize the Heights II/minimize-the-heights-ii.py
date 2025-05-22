#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        
        arr.sort()
        res = arr[-1] - arr[0]
        n=len(arr)-1
        
        for i in range(1,n+1):
            if arr[i] - k < 0:
                continue
            mine = min(arr[0]+k,arr[i]-k)
            maxe = max(arr[-1]-k,arr[i-1]+k)
            res = min(maxe-mine,res)
        
        return res