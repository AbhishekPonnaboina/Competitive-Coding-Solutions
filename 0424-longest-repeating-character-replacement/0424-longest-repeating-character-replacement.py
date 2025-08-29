class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        hashmap = [0]*26
        l,r =0,0
        maxfreq = 0

        while r < n:
            hashmap[ord(s[r])-ord('A')] += 1
            maxfreq = max(maxfreq,hashmap[ord(s[r])-ord('A')])

            while (r-l+1)- maxfreq > k:
                hashmap[ord(s[l])-ord('A')] -= 1
                maxfreq = max(maxfreq,hashmap[ord(s[l])-ord('A')])
                l += 1
            res = max(res,r-l+1)
            r += 1
            # if (r-l+1) - maxfreq <= k:
            #     res = max(res,r-l+1)
            #     r += 1
            # else:
            #     hashmap[ord(s[l])-ord('A')] -= 1
            #     maxfreq = max(maxfreq,hashmap[ord(s[l])-ord('A')])
            #     l += 1
        return res        
        










    
        #Naive approach but still got the time limited on a big case because you are generating every sunstring
        # res = 0
        # n = len(s)

        # for i in range(n):
        #     hashmap = [0]*26
        #     maxfreq = 0
        #     for j in range(i,n):
        #         hashmap[ord(s[j]) - ord('A')] += 1
        #         maxfreq = max(maxfreq,hashmap[ord(s[j]) - ord('A')] )
        #         conversions = (j-i+1)- maxfreq
        #         if conversions <= k:
        #             res = max(res,j-i+1)
        #         else:
        #             break
        # return res








        # this was your try and its busted
        # l,r = 0,0
        # n = len(s)
        # res = 0

        # while r < n:
        #     r = l
        #     cnt = k 
        #     for i in range(r,n+1):
        #         if s[i] == s[i+1]:
        #             r+= 1
        #         elif cnt > 0:
        #             r += 1
        #             cnt -= 1
        #         else:
        #             break
        #     res = max(res,r-l+1)
            
        #     for i in range(l,r+1):
        #         if s[i] != s[i+1]:
        #             break
        #         l += 1
        # return res
