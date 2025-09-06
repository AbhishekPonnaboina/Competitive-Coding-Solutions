class Solution:
    def myPow(self, x: float, n: int) -> float:
        #recursion approach
        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res =  (helper(x,n//2)) 
            res = ( res * res ) 
            if n % 2:
                return x * res
            return res
        
        ans = helper(x,abs(n))
        if n < 0:
            return 1/ans
        return ans
        #iteration approach
        # ans = 1.0000
        # nn = n
        # if nn < 0:
        #     nn = -1.0 * nn
        
        # while nn:
        #     if nn % 2 == 0:
        #         # print(ans)
        #         nn = nn // 2
        #         x = x * x
        #         # print("x ==",x)
        #     else:
                
        #         ans = ans * x
        #         # print(ans)
        #         nn = nn - 1
        # if n < 0:
        #     ans = 1.0 / ans
        # return ans

        #got the tleeee
        # res = 1.0
        # sign = 1
        # if n < 0:
        #     sign = -1
        #     n = -1 * n

        # for i in range(n):
        #     res = res * x   
        # if sign == -1:
        #     return 1/res
        # return res