class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = 1
        p1 = 0

        for i in range(1,len(nums)):
            if nums[p1] >= nums[i]:
                p1 += 1
                continue
            else:
                flag = 0
        if flag == 1:
            return True
        
        flag = 1
        p1 = 0
        for i in range(1,len(nums)):
            if nums[p1] <= nums[i]:
                p1 += 1
                continue
            else:
                flag = 0
        if flag == 1:
            return True
        return False