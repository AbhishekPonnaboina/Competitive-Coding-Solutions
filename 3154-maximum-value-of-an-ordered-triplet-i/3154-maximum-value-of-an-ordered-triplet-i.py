class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        first = nums[0]
        for i in range(1,n):
            if first < nums[i]:
                first = nums[i]
            for k in range(i+1,n):
                res = max(res,(first - nums[i])*nums[k])
        return res