from collections import defaultdict
class Solution:
    def totalElements(self, arr):
        # Code here
        l = 0
        n = len(arr)
        res = 0
        hashmap = defaultdict(int)
        
        for r in range(n):
            hashmap[arr[r]] += 1
            
            while len(hashmap) > 2:
                hashmap[arr[l]] -= 1
                if hashmap[arr[l]] == 0:
                    del hashmap[arr[l]]
                l += 1
            res = max(r-l+1,res)
        
        return res
            
        