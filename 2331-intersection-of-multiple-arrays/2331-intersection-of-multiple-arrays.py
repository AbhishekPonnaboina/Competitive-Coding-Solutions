from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        l = set(nums[0])

        for i in range(1,len(nums)):
            l = l & set(nums[i])
        l = list(l)
        l.sort()
        return l










        """myhash = defaultdict(int)
        reslen = len(nums)
        res = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                myhash[nums[i][j]] += 1
        
        for k,v in myhash.items():
            if v == reslen:
                res.append(k)

        res.sort()
        #print(res)
        
        return res"""

        