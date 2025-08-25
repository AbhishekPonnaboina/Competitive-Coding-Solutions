class Solution:
    def myAtoi(self, s: str) -> int:


        s = s.strip() 
        res = ""
        sign = True
        firstdigitcounter = False
        zeroc = False
        ans = 0
        signc = False



        for i in s:
            if not firstdigitcounter and i == "0":
                zeroc = True
                continue
            
            if i == '-' and not firstdigitcounter:
                if zeroc or signc:
                    break
                sign = False
                signc = True
                continue
            if i == '+' and not firstdigitcounter:
                if zeroc or signc :
                    break
                sign = True
                signc = True
                continue
            if ord(i) >= ord('0') and ord(i) <= ord("9"):
                res += i
                firstdigitcounter = True
            else:
                break
        rem = 1

        for i in range(len(res)-1,-1,-1):
            ans += int(res[i]) * rem
            rem *= 10

        if not sign :
            if -ans < -2**31 :
                return -2**31
            return -ans
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        return ans

                    


            



        