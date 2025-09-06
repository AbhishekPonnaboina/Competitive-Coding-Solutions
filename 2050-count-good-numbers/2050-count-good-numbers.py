import math 
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # better way to handle this is like is

        def helper(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res =  (helper(x,n//2)) % mod
            res = ( res * res ) % mod
            if n % 2:
                return x * res
            return res
        
        mod = 10 ** 9 + 7
        even = math.ceil(n/2)
        odd = math.floor(n/2)
        ans = (helper(5,even) * helper(4,odd)) % mod
        return ans




        #using the python inbuilt function but instead can work it through the pow(x,n) problem so lets use
        # that and solve
        # mod = 10 ** 9 + 7
        # even = math.ceil(n/2)
        # odd = math.floor(n/2)
        # result = (pow(5,even,mod) * pow(4,odd,mod)) % mod
        # return result
