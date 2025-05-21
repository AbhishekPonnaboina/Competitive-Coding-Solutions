# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        hashmap = {}
        res = 0
        psum = 0
        
        for i in range(len(arr)):
            psum += arr[i]
            
            if psum == k:
                res = i + 1
            
            if psum not in hashmap:
                hashmap[psum] = i
            
            if psum - k in hashmap:
                res = max(res,i - hashmap[psum-k])
        return res
    
