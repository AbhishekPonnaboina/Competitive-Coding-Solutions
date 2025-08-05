class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0

        for i in range(32):
            cnt = 0
            for j in nums:
                if j & (1 << i):
                    cnt += 1

            if cnt % 3 == 1:
                # print(res)
                res = res | (1 << i)
                # print(res)
        if res >= 2 ** 31 :
            res -= 2 ** 32
        return res