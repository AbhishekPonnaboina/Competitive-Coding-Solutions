class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill = 0
        valley = 0
        ele = 1

        while ele < len(nums)-1:
            print(nums[ele])
            left,right = ele,ele

            while left >= 0 and nums[left] == nums[ele]:
                left -= 1
            while right < len(nums) and nums[right] == nums[ele]:
                right += 1

            if left >= 0 and right <= len(nums)-1 and nums[left] < nums[ele] and nums[right] < nums[ele]:
                hill += 1

            elif left >= 0 and right <= len(nums)-1 and nums[left] > nums[ele] and nums[right] > nums[ele]:
                valley += 1               


            ele = right
        
        return hill + valley
