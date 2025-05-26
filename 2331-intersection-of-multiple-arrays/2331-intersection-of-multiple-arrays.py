from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        myhash = defaultdict(int)
        reslen = len(nums)
        res = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                myhash[nums[i][j]] += 1
        
        for k,v in myhash.items():
            if v == reslen:
                res.append(k)
        
        print(myhash)
        print(reslen)
        res.sort()
        #print(res)
        
        return res

        