class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(1,len(nums),3):
            if nums[i] != nums[i-1]:
                return nums[i-1]
        else:
            return nums[-1]











        #using bit wise bit counting method
        """res = 0

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
        return res"""