class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        left,right = 0,0
        myhash = dict()
        lena = 0
        
        while right < n:
            if s[right] in myhash and myhash[s[right]] >= left:
                left = myhash[s[right]] + 1
            
            lena = max(lena,right-left+1)
            myhash[s[right]] = right
            right += 1
        
        return lena
                
        