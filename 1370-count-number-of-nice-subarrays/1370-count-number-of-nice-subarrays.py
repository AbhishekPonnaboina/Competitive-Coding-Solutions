class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        #we can convert the oddds and even to 0 and 1 and use the 
        #strivers previous problem

        #this approach uses the three pointers approach thought by the 
        #neetcode 

        l,m =0,0
        odd = 0
        n = len(nums)
        res = 0

        for r in range(n):
            if nums[r] % 2 != 0:
                odd += 1
            
            print("right=",nums[r])
            
            while odd > k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l += 1
                m = l
            # print("left=",nums[l])
            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                print("middle=",nums[m])
                res += m - l + 1
        return res








        # n^2 approach yk its not gonna work right?
        # res = 0
        # n = len(nums)
        # for i in range(n):
        #     cnt = 0
        #     for j in range(i,n):
        #         if nums[j] % 2 == 1:
        #             cnt += 1
        #         if cnt ==k:
        #             res += 1
        # return res