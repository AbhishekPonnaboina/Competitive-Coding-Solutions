#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    # Function to calculate the span of stock's price for all n days.
    def calculateSpan(self, arr):
        #write code here
        stack = []
        stack.append(0)
        span = [1]
        
        for i in range(1,len(arr)):
            while (len(stack) > 0 and arr[stack[-1]] <= arr[i]) :
                stack.pop()
            if len(stack) == 0:
                span.append(i+1)
            else:
                span.append( i - stack[-1])
            stack.append(i)
        return span
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends