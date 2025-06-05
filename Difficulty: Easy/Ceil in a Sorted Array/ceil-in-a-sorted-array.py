#User function Template for python3
class Solution:
    def findCeil(self, arr, x):
        # code here
        res = -1 
        
        low,high = 0,len(arr)-1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return res
