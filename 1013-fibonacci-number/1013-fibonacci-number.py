class Solution:
    def fib(self, N: int) -> int:
        return round((pow(((math.sqrt(5)+1)/2),N))/math.sqrt(5))