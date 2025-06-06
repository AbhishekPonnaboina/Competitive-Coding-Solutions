class Solution:
    def countFreq(self, arr, target):
        #code here
        
        low,high = 0 , len(arr) - 1
        first,second = -1,-1
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1
        
        low,high = 0 , len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if arr[mid] > target:
                second = mid
                high = mid - 1
            else:
                low = mid + 1
        #print(first,second)
        if arr[-1] == target:
            second = len(arr)
        return second - first if first != -1 and second != -1 else 0
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countFreq(A, D)
        print(ans)
        print("~")

# } Driver Code Ends