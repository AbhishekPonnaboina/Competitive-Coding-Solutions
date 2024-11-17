#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, target):
        #Your code here
        
        res = 0
        mydict = defaultdict(int)
        pre_sum = 0
        
        for i in range(len(arr)):
            pre_sum += arr[i] 
            
            if pre_sum == target:
                res += 1
            if pre_sum - target in mydict:
                    res += mydict[pre_sum - target]
            mydict[pre_sum] += 1
        return res
                
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends