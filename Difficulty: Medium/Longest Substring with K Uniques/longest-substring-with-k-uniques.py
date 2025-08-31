from collections import defaultdict
class Solution:
    def longestKSubstr(self, s, k):
        # code here
        res = -1
        n = len(s)
        l = 0
        hashmap = defaultdict(int)
        
        for r in range(n):
            # print("-------")
            hashmap[s[r]] += 1
            
            
            
            while len(hashmap) > k:
                # print(hashmap)
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                l += 1
            
            if len(hashmap) == k:
                res = max(res,r-l+1)
                # print(res)
        
        return res
                
                
        
        
        
        
        
        
        
        
        
        # for l in range(n):
        #     hashmap = defaultdict(int)
        #     for r in range(l,n):
        #         hashmap[s[r]] += 1
        #         if len(hashmap) == k:
        #             res = max(res,r-l+1)
        #         if len(hashmap) > k:
        #             break
        # return res
            
        
        