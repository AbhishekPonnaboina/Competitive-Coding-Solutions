class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minlen = 2**31 - 1
        n= len(s)
        m = len(t)
        sidx = -1 #starting index
        eidx = n #ending index
        l = r = 0
        hashmap = Counter(t)
        cnt = 0
    
        for r in range(n):
            hashmap[s[r]] -= 1
            if hashmap[s[r]] >= 0:
                cnt += 1
                # hashmap[s[r]] -= 1
            
            while cnt == m:
                
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    sidx = l
                    eidx= r
                
                hashmap[s[l]] += 1

                if hashmap[s[l]] > 0:
                    cnt -= 1
                l += 1
            
        
        return "" if sidx == -1 else s[sidx:eidx+1]

                 















        #Got the ttle because of n^2 but just for the intuition
        # res = 2**31 - 1

        # n = len(s)
        # m = len(t)
        # sidx = -1 #starting index
        # eidx = n #ending index


        # for i in range(n):
        #     hashmap = Counter(t)
        #     cnt = 0
        #     for j in range(i,n):
        #         if hashmap[s[j]] > 0:
        #             hashmap[s[j]] -= 1
        #             cnt += 1
        #         if cnt == m:
        #             if res > j - i + 1:
        #                 res = j - i + 1
        #                 sidx = i
        #                 eidx = j
        #             break
        # if sidx == -1 and eidx == n:
        #     return ""
        # return s[sidx:eidx+1]



            
        


