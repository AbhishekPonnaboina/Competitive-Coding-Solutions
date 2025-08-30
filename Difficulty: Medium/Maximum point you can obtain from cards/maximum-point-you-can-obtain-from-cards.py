class Solution:
    def maxScore(self, nums, k):
        # code here.
        ans =  res = sum(nums[:k])
        n = len(nums)
        
        for i in range(k):
            ans -= nums[k-1-i]
            ans += nums[n-1-i]
            res = max(res,ans)
        
        return res