#User function Template for python3
class Solution:
    def upperBound(self, arr, target):
        #code here
        low , high = 0,len(arr)

        while low < high:
            mid = (low + high)// 2
            if arr[mid] <= target:
                low = mid + 1
                
            else:
                high = mid
        
        return low