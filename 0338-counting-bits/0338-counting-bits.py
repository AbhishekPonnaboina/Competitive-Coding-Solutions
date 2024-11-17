class Solution:
    def countBits(self, n: int) -> List[int]:
        #dp solution

        dp = [0]*(n+1)
        offset = 1

        for i in range(1,n+1):
            if offset*2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp














        """resa = []

        for i in range(n+1):
            res = 0
            while i:
                res += (i & 1)
                i = i // 2
            resa.append(res)
        return resa"""