#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        a = n
        ans = 0
        
        while a:
            mod = a % 10
            ans += mod ** 3
            a //= 10
    
        return ans == n
        