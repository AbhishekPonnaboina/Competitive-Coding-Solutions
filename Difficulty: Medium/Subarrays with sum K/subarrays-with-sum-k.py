from collections import defaultdict
class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0
        psum = 0
        
        for i in range(len(arr)):
            psum += arr[i]
            if psum - k in hashmap.keys():
                count += hashmap[psum-k]
            hashmap[psum] += 1
        
        return count 