class Solution:
    def minBitFlips(self, start: int, end: int) -> int:
        cnt = 0
        while start != end :
            n = start & 1
            print("n=",n)
            start = start >> 1
            p = end & 1
            print("p=",p)
            end = end >> 1
            if n != p:
                cnt += 1
        return cnt
        