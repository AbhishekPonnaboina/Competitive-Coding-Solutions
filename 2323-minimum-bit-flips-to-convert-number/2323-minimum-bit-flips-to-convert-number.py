class Solution:
    def minBitFlips(self, start: int, end: int) -> int:

        myxor = start ^ end
        cnt =0
        while myxor:
            #brian neighmans algorithm
            myxor = myxor & (myxor - 1)
            cnt += 1
        return cnt    

"""        cnt = 0
        while start != end :
            n = start & 1
            print("n=",n)
            start = start >> 1
            p = end & 1
            print("p=",p)
            end = end >> 1
            if n != p:
                cnt += 1"""
        
        