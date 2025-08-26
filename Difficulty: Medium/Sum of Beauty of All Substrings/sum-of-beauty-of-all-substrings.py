#User function Template for python3

class Solution:
    def beautySum(self, s):
        # Code here
        n = len(s)
        if n <= 1:
            return 0
        res = 0
        
        for i in range(n):
            freq = [0]*26
            for j in range(i,n):
                freq[ord(s[j])-ord('a')] += 1
                maxi = 0
                mini = float('inf')
                for f in freq:
                    if f > 0:
                        if f > maxi:
                            maxi = f
                        if f < mini:
                            mini = f
                res += maxi - mini
        return res
        