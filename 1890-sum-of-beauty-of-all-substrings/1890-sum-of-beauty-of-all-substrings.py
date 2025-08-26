class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        
        res = 0
        
        for i in range(n):
            freq = [0]*26
            # hashmap = collections.defaultdict(int)
            # hashmap[s[i]] = 1
            for j in range(i,n): #i+1
                idx = ord(s[j]) - ord("a")
                freq[idx] += 1
                #this is what worked in gfg and also its better than calulating max every time instead 
                #we could do only when value changes
                maxi = float("-inf")
                mini = float("inf")
                for fr in freq:
                    if fr > 0:
                        if fr > maxi:
                            maxi = fr
                        if fr < mini:
                            mini = fr 

                #this was the second approach
                # maxi = max(freq)
                # mini = min(x for x in freq if x > 0)

                                    #this was the first approach
                                    # maxi = max(hashmap.values())
                                    # mini = min(hashmap.values())
                res += maxi - mini
                
        return res


        