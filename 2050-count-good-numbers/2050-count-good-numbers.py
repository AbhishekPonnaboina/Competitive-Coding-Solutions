import math 
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        
        return ((5 ** math.ceil(n / 2)) * (4 ** math.floor(n/2))) % (10 ** 9 + 7) 