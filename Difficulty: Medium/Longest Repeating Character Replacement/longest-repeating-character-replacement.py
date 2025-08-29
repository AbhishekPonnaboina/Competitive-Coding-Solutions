#User function Template for python3

class Solution:
    def characterReplacement(self, s, k):
        # Code here
        l,r = 0,0
        hashmap = [0]*26
        maxfreq = 0
        res = 0
        n = len(s)
        while r < n:
            hashmap[ord(s[r])-ord('A')] += 1
            maxfreq = max(maxfreq,hashmap[ord(s[r])-ord('A')])
            
            if r-l+1 - maxfreq > k:
                hashmap[ord(s[l])-ord('A')] -= 1
                l += 1
            
            if r-l+1- maxfreq <= k:
                res = max(res,r-l+1)
            r += 1
        return res
                
                
                
                
                
                
                
                
                