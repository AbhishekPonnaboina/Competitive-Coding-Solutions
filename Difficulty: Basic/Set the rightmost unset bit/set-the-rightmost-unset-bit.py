import math

class Solution:
    def setBit(self, n):
        # Helper function to find position of rightmost set bit
        def setibit(n):
            return int(math.log2(n & -n) + 1)
        
        if n == 0:
            return 1
        

        
        pos = setibit(~n)
        
        return (1 << (pos - 1)) | n
