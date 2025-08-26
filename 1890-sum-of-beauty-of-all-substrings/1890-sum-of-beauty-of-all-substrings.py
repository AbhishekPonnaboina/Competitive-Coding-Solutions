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
                maxi = max(freq)
                mini = min(x for x in freq if x > 0)
                # maxi = max(hashmap.values())
                # mini = min(hashmap.values())
                res += maxi - mini
                
        return res


        