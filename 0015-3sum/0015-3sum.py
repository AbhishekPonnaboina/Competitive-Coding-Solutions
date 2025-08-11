class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        myhash = set()
        
        for i in range(len(nums)):
            if i > 0 and nums[i]== nums[i-1]:
                continue
            val = nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                
                tot = val + nums[left] + nums[right]
                if tot == 0:
                    myhash.add((val,nums[left],nums[right]))
                    left += 1
                    right -= 1
                elif tot > 0:
                    right -= 1
                else:
                    left += 1
        res = list(myhash)
        return res 