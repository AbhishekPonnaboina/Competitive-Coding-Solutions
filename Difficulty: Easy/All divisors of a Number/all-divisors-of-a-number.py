#User function Template for python3
import math
class Solution:
    def print_divisors(self, n):
        # code here
        ans = set()
        for i in range(1,int(math.sqrt(n)+1)):
            if n % i == 0:
                ans.add(i)
                ans.add(n//i)
                
        ans = list(ans)
        ans.sort()
        for i in ans:
            print(i,end=' ')
        