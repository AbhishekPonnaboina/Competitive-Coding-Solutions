class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue
            lef,righ = i + 1,len(nums)-1

            while lef < righ:
                sum3 = a + nums [lef] + nums[righ]
                if sum3 == 0:
                    res.append([a,nums[lef],nums[righ]])
                    lef += 1
                    while nums[lef] == nums[lef - 1] and lef < righ:
                        lef += 1
                elif sum3 > 0:
                    righ -= 1
                else:
                    lef += 1
        return res 

        

        
        
        
        
        
        
        
        
        
        
        
        """for i in range(size):
            l,r = i + 1 , size - 1

            if nums[i] == nums[l] or nums[l] == nums[r] or nums[r] == nums[i]:
                continue

            while l < r:
                if nums[l] + nums[r] == i:
                    result.append([i,l,r])
"""


        return set(result)

            
        
