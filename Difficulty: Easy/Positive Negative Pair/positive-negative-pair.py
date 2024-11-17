#User function Template for python3

class Solution:
    #Function to return list containing all the pairs having both
    #negative and positive values of a number in the array.
    def findPairs(self,arr,n):
        # code here 
        myhash = dict()
        res = []
        
        
        for i in arr:
            if -(i) in myhash:
                res.append(-abs(i))
                res.append(abs(i))
            else:
                myhash[i] = 1
               
        return res
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        res=Solution().findPairs(arr,n)
        if len(res) == 0:
            print(0)
        else:    
            for x in res:
                print(x,end=' ')
            print()
# } Driver Code Ends