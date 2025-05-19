class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        fir = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == fir:              
                continue
            fir = nums[i]
            nums[i],nums[count] = nums[count],nums[i]
            count += 1

        del nums[count:]
        return len(nums)
