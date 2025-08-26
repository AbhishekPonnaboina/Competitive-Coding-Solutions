class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        
        res = 0
        
        for i in range(n):
            hashmap = collections.defaultdict(int)
            hashmap[s[i]] = 1
            for j in range(i+1,n):
                hashmap[s[j]] += 1
                maxi = max(hashmap.values())
                mini = min(hashmap.values())
                res += maxi - mini
                
        return res


        