class Solution:
    def countBits(self, n: int) -> List[int]:
        
        resArr = []*(n+1)

        for i in range(n+1):
            res = 0
            while i:
                res += 1
                i = i & i - 1
            resArr.append(res)
        return resArr