#User function Template for python3

class Solution:
    def searchInsertK(self, arr, N, k):
        # code here
        low = 0
        high = len(arr) - 1
        res =  len(arr)
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res