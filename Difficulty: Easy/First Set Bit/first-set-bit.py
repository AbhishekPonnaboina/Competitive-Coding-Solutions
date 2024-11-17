#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Function to find position of first set bit in the given number.
    def getFirstSetBit(self,n):
        #Your code here
        
        counta = 0
        
        while n:
            counta += 1
            if (n & 1):
                return counta
            n = n >> 1
            
        return 0
                
                
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        ob=Solution()
        
        print(ob.getFirstSetBit(n))
        
        
        T-=1
        print("~")
    
    




if __name__=="__main__":
    main()
# } Driver Code Ends