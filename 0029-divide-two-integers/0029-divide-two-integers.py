class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div = dividend
        by = divisor
        sign = True

        if div == by:
            return 1
        if (div >= 0 and by < 0) or (div < 0 and by > 0)  :
            sign = False
        
        n = abs(div)
        d = abs(by)
        ans = 0

        while n >= d :
            cnt = 0 
            while (n >= d << (cnt + 1)): 
                
                # here the d is getting multiplied with the help of the cnt which is increasing by every 2 power of i's so we find the largest possible and then we subtract it from it 
                cnt += 1
            ans += 1 << cnt
            n -= d << cnt

        if ans >= 2**31 and sign == True:
            return 2**31 - 1
        if ans >= 2**31 and sign == False:
            return - (2 ** 31)
        
        return ans if sign == True else  -ans 