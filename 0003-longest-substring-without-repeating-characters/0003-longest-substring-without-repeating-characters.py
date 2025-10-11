class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #better approach
        maxlena = 0
        n = len(s)
        i,j = 0,0
        hashmap = dict()

        while j < n:
            if s[j] in hashmap and hashmap[s[j]] >= i:
                    i = hashmap[s[j]] + 1
                    # print(hashmap)
                    
            maxlena = max(maxlena,j-i+1)
            hashmap[s[j]] = j
            j += 1
        
        return maxlena
        #naive approach
        # n = len(s)
        # maxlen = 0

        # for i in range(n):
        #     myhash = defaultdict(int)
        #     for j in range(i,n):
        #         if myhash[s[j]] == 1:
        #             break
        #         lena = j - i + 1
        #         maxlen = max(lena,maxlen)
        #         myhash[s[j]] = 1
        # return maxlen

        