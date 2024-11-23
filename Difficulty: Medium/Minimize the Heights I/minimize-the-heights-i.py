#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        
        n = len(arr)
        arr.sort()


        diff = arr[-1] - arr[0]
    
        for i in range(n - 1):
            maxht = max(arr[i] + k, arr[-1] - k)
        
            minht = min(arr[0] + k, arr[i + 1] - k)
    
            diff = min(diff, maxht - minht)
    
        return diff


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends