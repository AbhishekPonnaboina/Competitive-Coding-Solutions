#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        myhash = set()
        pre_sum = 0
        
        for i in range(len(arr)):
            pre_sum += arr[i]
            
            if pre_sum == 0 or pre_sum in myhash:
                return True
            myhash.add(pre_sum)
        return False
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr)):
            print("true")
        else:
            print("false")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends