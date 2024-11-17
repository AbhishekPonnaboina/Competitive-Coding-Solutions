#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        ##Your code here
        
        counta = 0
        res = 0
        while N:
            if (N%2) == 1:
                counta += 1
                res = max(res,counta)
            else:
                counta = 0
            N = N // 2 
        return res
        
        
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends