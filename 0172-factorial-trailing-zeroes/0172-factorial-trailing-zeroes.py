class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fib(n):
            if n == 0:
                return 0
            elif n == 1:
                return 1
            return n*fib(n-1)
        
        fact = fib(n)
        rescnt = 0
        dup = fact

        while dup:
            rem = dup % 10
            if rem > 0:
                break
            if rem == 0:
                rescnt += 1
            dup //= 10
        
        return rescnt