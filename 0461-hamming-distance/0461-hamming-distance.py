class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = x ^ y
        counti = 0
        while res:
            counti += 1
            res = res & (res-1)
        return counti 