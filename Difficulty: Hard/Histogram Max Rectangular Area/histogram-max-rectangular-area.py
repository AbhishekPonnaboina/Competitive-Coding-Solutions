#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,arr):
        #code here
        stack = []
        res = 0
        
        for i in range(len(arr)):
            
            while (stack and arr[stack[-1]] >= arr[i]):
                tp = stack[-1]
                stack.pop()
                if stack:
                    currwidth = i - stack[-1] - 1
                else:
                    currwidth = i
                res = max(res,currwidth*arr[tp])
            stack.append(i)
        
        while stack:
            tp = stack[-1]
            stack.pop()
            if stack:
                currwidth = len(arr) - stack[-1] - 1 
            else:
                currwidth = len(arr)
            res = max(res,currwidth*arr[tp])
        return res
        
        
        
        
        
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
        print("~")
# } Driver Code Ends