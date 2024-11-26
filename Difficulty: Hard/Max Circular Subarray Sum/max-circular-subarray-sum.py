#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):

    
    ##Your code here
    n = len(arr)
    a, b = arr[0], arr[0]
    c, d = arr[0], arr[0]
    e = arr[0]
    
    for i in range(1, n):
        b = max(arr[i], b + arr[i])
        a = max(a, b)
        
        d = min(arr[i], d + arr[i])
        c = min(c, d)
        
        e += arr[i]
    
    if a < 0:
        return a
    
    return max(a, e - c)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
import sys

if __name__ == "__main__":
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        print(circularSubarraySum(arr))

        T -= 1

# } Driver Code Ends