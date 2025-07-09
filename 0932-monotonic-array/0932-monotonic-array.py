class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        incflag = 1
        decflag = 1

        for i in range(1,len(nums)):
            if not (nums[i] <= nums[i-1]):
                decflag = 0
            if not (nums[i] >= nums[i-1]):
                incflag = 0
        if incflag or decflag:
            return True
        return False

