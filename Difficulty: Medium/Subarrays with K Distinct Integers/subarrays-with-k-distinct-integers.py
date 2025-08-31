#User function Template for python3
from collections import defaultdict
class Solution:
    def exactlyK(self, nums, k):
        # Code here
        hashmap = defaultdict(int)
        l= m = 0
        n = len(arr)
        res =0
        for r in range(n):
            hashmap[nums[r]] += 1
            
            
            while len(hashmap) > k:
                hashmap[nums[m]] -= 1
                if hashmap[nums[m]] == 0:
                    del hashmap[nums[m]]
                m += 1
                l = m
                
            while hashmap[nums[m]] > 1:
                hashmap[nums[m]] -= 1
                m += 1
                
            if len(hashmap) == k:
                res += (m-l+1)
        return res
                