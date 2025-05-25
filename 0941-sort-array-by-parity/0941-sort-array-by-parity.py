class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i,j = 0,len(nums) - 1

        while i < j  :
            while nums[i]%2 == 0 and i < j:
                i += 1
            while nums[j]%2 != 0 and i < j :
                j -= 1
            if i < j:
                nums[i],nums[j] = nums[j],nums[i]
        
        return nums

        