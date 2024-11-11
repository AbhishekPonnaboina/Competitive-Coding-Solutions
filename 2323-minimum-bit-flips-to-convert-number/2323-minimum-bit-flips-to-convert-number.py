class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        minflip = 0
        n = start ^ goal
        while n:
            n = n & (n-1)
            minflip += 1
        return minflip