class Solution:
    def countBits(self, n: int) -> List[int]:
        resa = []

        for i in range(n+1):
            res = 0
            while i:
                res += (i & 1)
                i = i // 2
            resa.append(res)
        return resa