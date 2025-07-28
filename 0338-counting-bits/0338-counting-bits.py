class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dparr = [0]*256

        for i in range(256):
            # print(i&1)
            dparr[i] = (i & 1) + dparr[i>>1]
        
        resArr = []*(n+1)

        for i in range(n+1):
            resArr.append(
                dparr[i & 0xff] +
                dparr[i>>8 & 0xff] +
                dparr[i>>16 & 0xff] +
                dparr[i>>24 & 0xff]
            )
        return resArr
        

        