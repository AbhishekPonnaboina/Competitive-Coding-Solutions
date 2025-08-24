class Solution:
    def frequencySort(self, s: str) -> str:
        myhash = dict()
        resstr = ""


        for i in range(len(s)):
            myhash[s[i]] = myhash.get(s[i],0) + 1
        
        res = sorted(myhash.items(),key = lambda x:x[1],reverse=True)
        
        for i in res:
            key,val = i
            resstr += key*val
        
        return resstr