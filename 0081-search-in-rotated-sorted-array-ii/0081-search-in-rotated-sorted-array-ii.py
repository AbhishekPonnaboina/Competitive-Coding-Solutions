class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lina = len(nums) - 1
        left = 0
        right = lina

        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                return True 
            if nums[left] == nums[mid] :
                left = left + 1
                continue
            if nums[right] == nums[mid] :
                right = right - 1
                continue

            
            elif nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False 
        