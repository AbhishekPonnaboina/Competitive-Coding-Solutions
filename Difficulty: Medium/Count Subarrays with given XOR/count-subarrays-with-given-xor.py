from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        
        myhash = defaultdict(int)
        pxor = 0
        myhash[0] = 1
        count = 0
        
        for i in range(len(arr)):
            pxor = pxor ^ arr[i]
            ele = pxor^k
            if ele in myhash.keys():
                count += myhash[ele]
            myhash[pxor] += 1
        
        

        return count