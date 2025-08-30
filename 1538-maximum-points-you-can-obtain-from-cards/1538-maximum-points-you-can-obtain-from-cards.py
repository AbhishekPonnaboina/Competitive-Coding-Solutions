class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        ans = sum(nums[:k])
        n = len(nums)
        # for i in range(k):
        #     ans += nums[i]
        res = ans
        # print(ans)
        for i in range(k):
            ans -= nums[k-1-i]
            # print("before=",ans)
            ans += nums[n-1-i]
            # print("After=",ans)
            res = max(ans,res)


        return res
        