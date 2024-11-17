#User function Template for python3
from collections import defaultdict
class Solution:
    
    #Function to count subarrays with 1s and 0s.
    def countSubarrWithEqualZeroAndOne(self,arr, n):
        #Your code here
        res = 0
        mydict = defaultdict(int)
        mydict[0] = 1
        pre_sum = 0
        
        for i in range(len(arr)):
            if arr[i] == 0 :
                arr[i] = -1
        
        for i in range(len(arr)):
            pre_sum += arr[i]
            
            if pre_sum in mydict:
                res += mydict[pre_sum]
                
            mydict[pre_sum] += 1
                
        

        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        
        obj = Solution()
        print(obj.countSubarrWithEqualZeroAndOne(arr, n))
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends