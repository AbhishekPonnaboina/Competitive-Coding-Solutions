class Solution:
    def myAtoi(self, s: str) -> int:
        #recursion Implementation almost same just changing the while loop
        s = s.strip()
        if not s:
            return 0
        sign = 1
        ans = 0
        i = 0

        if s[0] in ['-','+']:
            if s[0] == '-':
                sign = -1
            i += 1
        
        def helper(i,ans=0):
            if i >= len(s) or not s[i].isdigit():
                return ans
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            if sign == 1 and ans >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            if sign == -1 and ans >= 2 ** 31:
                return 2 ** 31
            return helper(i+1,ans)
        res = 0 + helper(i,0)

        return sign * res



        #this is for the string implementation i guess
        s = s.strip()
        if not s:
            return 0
        sign = 1
        ans = 0
        i = 0

        if s[0] in ['-','+']:
            if s[0] == '-':
                sign = -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            if sign == 1 and ans >= 2 ** 31 -1:
                return 2 ** 31 -1
            if sign == -1 and ans >= 2 ** 31:
                return -2 ** 31
            i += 1
        
        return sign * ans

        # s = s.strip() 
        # # res = ""
        # # sign = True
        # # firstdigitcounter = False
        # # zeroc = False
        # # not required can be processed during the answer calculation
        # ans = 0
        # signc = False



        # for i in s:
        #     if not firstdigitcounter and i == "0":
        #         zeroc = True
        #         continue
            
        #     if i == '-' and not firstdigitcounter:
        #         if zeroc or signc:
        #             break
        #         sign = False
        #         signc = True
        #         continue
        #     if i == '+' and not firstdigitcounter:
        #         if zeroc or signc :
        #             break
        #         sign = True
        #         signc = True
        #         continue
        #     if ord(i) >= ord('0') and ord(i) <= ord("9"):
        #         res += i
        #         firstdigitcounter = True
        #     else:
        #         break
        # rem = 1

        # for i in range(len(res)-1,-1,-1):
        #     ans += int(res[i]) * rem
        #     rem *= 10

        # if not sign :
        #     if -ans < -2**31 :
        #         return -2**31
        #     return -ans
        # if ans > 2 ** 31 - 1:
        #     return 2 ** 31 - 1
        # return ans

                    


            



        