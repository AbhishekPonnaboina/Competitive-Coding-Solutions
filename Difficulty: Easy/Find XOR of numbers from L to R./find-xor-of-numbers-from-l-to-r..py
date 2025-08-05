#User function Template for python3

class Solution:
    def findXOR(self, l, r):
        # Code here
        def calxor(n):
            if n % 4 == 1:
                return 1
            elif n % 4  == 2:
                return n + 1
            elif n % 4 == 3:
                return 0
            else:
                return n

        
        return calxor(l-1) ^ calxor(r)