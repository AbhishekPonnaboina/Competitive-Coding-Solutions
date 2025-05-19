class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #two pointer
        left = 1
        right = 1

        while right < len(nums):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1
            right += 1

             
        del nums[left:]
        return len(nums)
        


        #your way
        """fir = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == fir:              
                continue
            fir = nums[i]
            nums[i],nums[count] = nums[count],nums[i]
            count += 1

        del nums[count:]
        return len(nums)"""