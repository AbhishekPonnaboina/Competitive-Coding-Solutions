class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        r,l = 0,0
        zeros = 0
        res = 0

        while r < n:
            if nums[r]==0:
                zeros += 1
                
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            res = max(r-l+1,res)
            r += 1
        return res
            
        
        # below solution didnt work and thats because of TLE
        # res = 0
        # n =  len(nums)
        # for i in range(n):
        #     igncnt = k
        #     j = i
        #     # print("im starting at here",nums[i])
        #     while j < n :
        #         if nums[j] == 1 :
        #             j += 1
        #         elif igncnt > 0:
        #             igncnt -= 1
        #             j += 1
        #         else:
        #             break
        #     # print("I stopped at here",nums[j])

        #     res = max(j-1-i+1,res)
        # return res



        














