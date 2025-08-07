#User function Template for python3


class Solution:
    def factorial (self, n):
        # code here
        # if n == 1:
        #     return 1
        # return n * self.factorial(n-1)
        
        fact = 1
        
        for i in range(1,n+1):
            fact *= i
        
        return fact