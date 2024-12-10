#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x:x[1])
        end=float('-inf')
        count=0
        for interval in intervals:
            if interval[0]<end:
                count+=1
            else:
                end=interval[1]
        return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends