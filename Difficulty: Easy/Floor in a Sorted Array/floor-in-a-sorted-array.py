class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        res = -1
        low,high = 0 , len(arr) - 1
        
        while low <= high:
            mid = (low + high)//2
            if arr[mid] <= x :
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res if res != -1 else -1